#!/usr/bin/env python3
"""
Base de radars Europe (OpenStreetMap) pour l'application VEKTRA.

Lancé chaque semaine par .github/workflows/radars.yml. Interroge Overpass tuile par tuile,
classe chaque radar EXACTEMENT comme l'application, supprime les doublons et écrit :

  radars/radars_europe.txt   format 1 (applications jusqu'à la 2.5.0) :
      TYPE;LAT;LON;VITESSE;ROUTE
  radars/radars_v2.txt       format 2 (à partir de la 2.5.0-alfa2) :
      TYPE;LAT;LON;VITESSE;ROUTE;AXE;SENS;CLASSE;FIN_LAT;FIN_LON

  TYPE    F = fixe, S = tronçon, R = feu rouge, M = mobile
  VITESSE limite en km/h, 0 si inconnue
  AXE     orientation de la route au radar, 0-179°, -1 si inconnue
  SENS    sens de circulation contrôlé, 0-359°, -1 si inconnu (ou les deux sens)
  CLASSE  m = autoroute / voie rapide, p = route principale, l = route locale, vide si inconnue
  FIN_*   fin du tronçon (radars tronçons) ; vide sinon. Pour un tronçon, LAT/LON = début.
  radars/radars_v3.txt       format 3 (à partir de la 2.6.2-alfa5) : format 2 + SOURCE
      SOURCE  O = OpenStreetMap, A = MapAtlas, OA = présent dans les deux (fiche OSM gardée)

MapAtlas Camera Index (https://mapatlas.eu, licence CC BY 4.0) : relevé figé, téléchargé pays
par pays seulement quand une nouvelle publication sort, puis gardé dans radars/mapatlas_europe.txt.
Ses radars n'ont ni orientation de route ni sens contrôlé fiable : AXE et SENS restent à -1, et
ses tronçons n'ont qu'un point (pas de début ni de fin).

Les radars déjà connus (fichiers existants) sont conservés s'ils manquent au téléchargement :
une panne de serveur ne fait jamais disparaître de radars.

Usage :
  build_radars.py weekly <dossier>            # tout : téléchargement, fusion, deux formats, fiches
  build_radars.py meta <base.txt> <meta.json> # fiche de version seule
  build_radars.py v3 <dossier>                # format 3 seul, depuis radars_v2.txt + MapAtlas
"""
import hashlib
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request

ENDPOINTS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.openstreetmap.fr/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
]
LATS = [34, 44, 54, 64, 72]
LONS = [-25, -15, -5, 5, 15, 25, 35, 45]
MIN_RADARS = 5000
DEDUP_METERS = 85.0
ROAD_MATCH_METERS = 25.0
DEADLINE = time.time() + float(os.environ.get("RADARS_MINUTES", "22")) * 60

# MapAtlas : pays (codes du catalogue) qui touchent la zone Europe de la base (34→72 N, -25→45 E).
# Les points hors de cette zone sont ignorés, comme pour OpenStreetMap.
MAPATLAS_URL = "https://mapatlas.eu/data/camera-index/"
MAPATLAS_CODES = (
    "AD AL AM AT AZ BA BE BG BY CH CY CZ DE DK DZ EE ES FI FR GB GE GI GR HR HU IE IQ IR IS IT "
    "LB LI LT LU LV MA MC MD ME MK MT NL NO PL PT RO RS RU SE SI SK SM SY TN TR UA XK"
).split()
MAPATLAS_CLASS = {"spot": "F", "adaptive": "F", "signal": "R", "corridor": "S"}

MOTORWAY = {"motorway", "motorway_link", "trunk", "trunk_link"}
PRINCIPAL = {"primary", "primary_link", "secondary", "secondary_link"}
ROADS = ("motorway|motorway_link|trunk|trunk_link|primary|primary_link|secondary|secondary_link|"
         "tertiary|tertiary_link|unclassified|residential|living_street|service|road")


# ── Outils géographiques ────────────────────────────────────────────────────

def dist_m(la1, lo1, la2, lo2):
    p1, p2 = math.radians(la1), math.radians(la2)
    dp, dl = p2 - p1, math.radians(lo2 - lo1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 6371000.0 * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def bearing(la1, lo1, la2, lo2):
    p1, p2 = math.radians(la1), math.radians(la2)
    dl = math.radians(lo2 - lo1)
    y = math.sin(dl) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    return (math.degrees(math.atan2(y, x)) + 360.0) % 360.0


def seg_distance(lat, lon, a, b):
    """Distance (m) d'un point au segment a-b, en projection locale plane."""
    k = math.cos(math.radians(lat)) * 111320.0
    ax, ay = (a[1] - lon) * k, (a[0] - lat) * 110540.0
    bx, by = (b[1] - lon) * k, (b[0] - lat) * 110540.0
    dx, dy = bx - ax, by - ay
    l2 = dx * dx + dy * dy
    t = 0.0 if l2 == 0 else max(0.0, min(1.0, -(ax * dx + ay * dy) / l2))
    px, py = ax + t * dx, ay + t * dy
    return math.hypot(px, py)


# ── Requêtes Overpass ───────────────────────────────────────────────────────

def http(query, label, timeout, endpoints=None):
    data = urllib.parse.urlencode({"data": query}).encode()
    for ep in (endpoints or ENDPOINTS):
        if time.time() > DEADLINE:
            print(f"  {label} : temps écoulé, abandon", flush=True)
            return None
        try:
            req = urllib.request.Request(ep, data=data, headers={
                "User-Agent": "VektraBuild/1.0 (BYD cockpit, offline radar base)",
                "Referer": "https://overpass-turbo.eu/",
            })
            with urllib.request.urlopen(req, timeout=timeout + 20) as r:
                body = json.loads(r.read().decode("utf-8"))
            if "runtime error" in str(body.get("remark", "")):
                raise RuntimeError(body["remark"])
            els = body.get("elements", [])
            print(f"  {label} -> {len(els)} éléments ({ep})", flush=True)
            return els
        except Exception as ex:
            print(f"  {label} : échec {ep} ({ex})", flush=True)
            time.sleep(5)
    return None


def q_relations(b, t):
    return f'[out:json][timeout:{t}];relation["enforcement"]{b};out geom qt;'


def q_nodes_with_roads(b, t):
    # Radars + routes qui les portent, avec leur tracé. (La recherche « à moins de 25 m » faisait
    # dépasser le délai des serveurs sur les zones denses : seuls les radars posés sur la route
    # reçoivent une orientation ; les autres gardent le sens donné par les relations.)
    return (f"[out:json][timeout:{t}];"
            f'(node["highway"="speed_camera"]{b};node["highway"="speed_display"]["speed_camera"]{b};)->.c;'
            ".c out qt;"
            f'way(bn.c)["highway"~"^({ROADS})$"];'
            "out tags geom qt;")


def q_nodes_only(b, t):
    return (f"[out:json][timeout:{t}];"
            f'(node["highway"="speed_camera"]{b};node["highway"="speed_display"]["speed_camera"]{b};);out qt;')


def split(b):
    s_, w, n, e = (float(x) for x in b.strip("()").split(","))
    ms, mw = (s_ + n) / 2, (w + e) / 2
    return [f"({a},{c},{bb},{d})" for a, bb in ((s_, ms), (ms, n)) for c, d in ((w, mw), (mw, e))]


FAILED_BOXES = []


def in_box(r, b):
    s_, w, n, e = (float(x) for x in b.strip("()").split(","))
    return s_ <= r["lat"] <= n and w <= r["lon"] <= e


def fetch_nodes(b, size, records):
    """Radars d'une zone avec leurs routes ; zone trop lourde = coupée en 4 (jusqu'à 2,5°)."""
    # Zone encore grande : un seul serveur essayé avant de la découper (gagne du temps).
    eps = ENDPOINTS[:1] if size > 2.5 else None
    els = http(q_nodes_with_roads(b, 170), f"radars + routes {b}", 170, eps)
    if els is None and size > 2.5 and time.time() < DEADLINE:
        ok = True
        for sub_b in split(b):
            ok = fetch_nodes(sub_b, size / 2, records) and ok
        return ok
    if els is None:
        els = http(q_nodes_only(b, 120), f"radars seuls {b}", 120)
    if els is None:
        FAILED_BOXES.append(b)
        return False
    roads = RoadIndex()
    for el in els:
        if el.get("type") == "way":
            roads.add_way(el)
    for el in els:
        if el.get("type") == "node":
            r = from_node(el, roads)
            if r:
                records.append(r)
    time.sleep(1)
    return True


def tiles():
    for i in range(len(LATS) - 1):
        for j in range(len(LONS) - 1):
            yield f"({LATS[i]},{LONS[j]},{LATS[i + 1]},{LONS[j + 1]})"


# ── Classement (copie fidèle de l'application) ──────────────────────────────

def classify(tags):
    g = lambda k: str(tags.get(k, "")).lower()
    highway, enforcement, construction = g("highway"), g("enforcement"), g("construction")
    cam_type, cam_mount, speed_cam = g("camera:type"), g("camera:mount"), g("speed_camera")
    text = g("name") + " " + g("description") + " " + g("note")
    if highway == "construction" or construction:
        return "W"
    if (enforcement in ("average_speed", "section") or highway == "average_speed_camera"
            or cam_type == "average_speed" or speed_cam in ("average_speed", "section")
            or any(w in text for w in ("tronçon", "troncon", "traject", "section", "average"))):
        return "S"
    if (enforcement == "traffic_signals" or "red_light" in enforcement or "signal" in enforcement
            or "red_light" in cam_type or "traffic_signals" in speed_cam or "red_light" in speed_cam
            or tags.get("traffic_signals:camera", "") == "yes"):
        return "R"
    if (enforcement == "check" or cam_mount == "mobile" or cam_type == "mobile"
            or speed_cam == "mobile" or tags.get("temporary", "") == "yes"):
        return "M"
    if highway == "speed_camera" or enforcement in ("maxspeed", "speed") or cam_type in ("fixed", "speed"):
        return "F"
    return None


def max_speed(tags):
    digits = "".join(c for c in str(tags.get("maxspeed", "")) if c.isdigit())
    v = int(digits) if digits else 0
    return v if 20 <= v <= 140 else 0


def road_class(highway):
    if highway in MOTORWAY:
        return "m"
    if highway in PRINCIPAL:
        return "p"
    return "l" if highway else ""


def clean(s):
    return str(s or "").replace(";", ",").replace("\n", " ").strip()[:40]


# ── Index des routes autour des radars ──────────────────────────────────────

class RoadIndex:
    CELL = 0.002

    def __init__(self):
        self.grid = {}

    def add_way(self, way):
        geom = way.get("geometry") or []
        hw = (way.get("tags") or {}).get("highway", "")
        ref = (way.get("tags") or {}).get("ref") or (way.get("tags") or {}).get("name") or ""
        pts = [(p["lat"], p["lon"]) for p in geom if p and "lat" in p]
        for a, b in zip(pts, pts[1:]):
            seg = (a, b, hw, ref)
            # Toutes les cases traversées par le segment (pas d'une demi-case).
            n = int(max(abs(b[0] - a[0]), abs(b[1] - a[1])) / (self.CELL / 2)) + 1
            cells = set()
            for i in range(n + 1):
                la = a[0] + (b[0] - a[0]) * i / n
                lo = a[1] + (b[1] - a[1]) * i / n
                cells.add((int(la // self.CELL), int(lo // self.CELL)))
            for c in cells:
                self.grid.setdefault(c, []).append(seg)

    def candidates(self, lat, lon, radius):
        """Segments à moins de [radius] m, triés du plus proche au plus loin."""
        cx, cy = int(lat // self.CELL), int(lon // self.CELL)
        out, seen = [], set()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for seg in self.grid.get((cx + dx, cy + dy), ()):
                    if id(seg) in seen:
                        continue
                    seen.add(id(seg))
                    d = seg_distance(lat, lon, seg[0], seg[1])
                    if d <= radius:
                        out.append((d, seg))
        out.sort(key=lambda x: x[0])
        return out

    def nearest(self, lat, lon):
        cx, cy = int(lat // self.CELL), int(lon // self.CELL)
        best = None
        seen = set()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for seg in self.grid.get((cx + dx, cy + dy), ()):
                    if id(seg) in seen:
                        continue
                    seen.add(id(seg))
                    d = seg_distance(lat, lon, seg[0], seg[1])
                    if best is None or d < best[0]:
                        best = (d, seg)
        if best is None or best[0] > ROAD_MATCH_METERS:
            return None
        return best[1]


# ── Construction des fiches radar ───────────────────────────────────────────

def from_relation(rel):
    """Radar porté par une relation « enforcement » (sens fiable : du point from vers le radar)."""
    tags = rel.get("tags") or {}
    t = classify(tags)
    if t is None or t == "W":
        return None
    members = rel.get("members") or []

    def first(role):
        for m in members:
            if m.get("role") == role and m.get("type") == "node" and "lat" in m:
                return m["lat"], m["lon"]
        return None

    device, frm, to = first("device"), first("from"), first("to")
    speed = max_speed(tags)
    ref = clean(tags.get("ref") or tags.get("name"))
    if t == "S" and frm and to:
        d = int(round(bearing(frm[0], frm[1], to[0], to[1])))
        return dict(t="S", lat=frm[0], lon=frm[1], spd=speed, ref=ref, axe=-1, sens=d, cls="",
                    end=(to[0], to[1]))
    pos = device or frm
    if pos is None:
        pts = [(m["lat"], m["lon"]) for m in members if "lat" in m]
        if not pts:
            return None
        pos = (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
    sens = -1
    if frm and device and dist_m(frm[0], frm[1], device[0], device[1]) > 5:
        sens = int(round(bearing(frm[0], frm[1], device[0], device[1])))
    return dict(t=t, lat=pos[0], lon=pos[1], spd=speed, ref=ref, axe=-1, sens=sens, cls="", end=None)


def from_node(node, roads):
    tags = node.get("tags") or {}
    t = classify(tags)
    if t is None or t == "W":
        return None
    lat, lon = node.get("lat"), node.get("lon")
    if lat is None or lon is None:
        return None
    axe, sens, cls, ref = -1, -1, "", clean(tags.get("ref") or tags.get("name"))
    seg = roads.nearest(lat, lon) if roads else None
    if seg:
        fwd = bearing(seg[0][0], seg[0][1], seg[1][0], seg[1][1])
        axe = int(round(fwd)) % 180
        cls = road_class(seg[2])
        if not ref:
            ref = clean(seg[3])
        d = str(tags.get("direction", "")).lower()
        # Seuls forward/backward (relatifs au sens de dessin de la route) sont fiables.
        if d == "forward":
            sens = int(round(fwd)) % 360
        elif d == "backward":
            sens = int(round(fwd + 180)) % 360
    return dict(t=t, lat=lat, lon=lon, spd=max_speed(tags), ref=ref, axe=axe, sens=sens, cls=cls, end=None,
                nid=node.get("id"))


def q_roads_around(ids, t):
    return (f"[out:json][timeout:{t}];node(id:{','.join(str(i) for i in ids)})->.c;"
            f'way(around.c:{int(ROAD_MATCH_METERS)})["highway"~"^({ROADS})$"];out tags geom qt;')


def roads_near_off_road(records):
    """
    Radars posés à côté de la route (pas sur elle) : on cherche les routes à moins de 25 m,
    par lots de 250 radars. Si deux routes différentes sont presque aussi proches (moins de
    6 m d'écart) avec des orientations différentes, le radar est ambigu (carrefour, bretelle) :
    on ne devine pas, il reste sans orientation.
    """
    todo = [r for r in records if r.get("nid") and r["axe"] < 0 and r["t"] != "S"]
    print(f"Radars à côté de la route : {len(todo)} à rattacher", flush=True)
    found = ambiguous = 0
    for k in range(0, len(todo), 250):
        if time.time() > DEADLINE:
            print("  routes voisines : temps écoulé, arrêt", flush=True)
            break
        batch = todo[k:k + 250]
        els = http(q_roads_around([r["nid"] for r in batch], 120), f"routes voisines {k // 250 + 1}", 120)
        if els is None:
            continue
        idx = RoadIndex()
        for el in els:
            if el.get("type") == "way":
                idx.add_way(el)
        for r in batch:
            cands = idx.candidates(r["lat"], r["lon"], ROAD_MATCH_METERS)
            if not cands:
                continue
            d0, seg0 = cands[0]
            axe0 = int(round(bearing(seg0[0][0], seg0[0][1], seg0[1][0], seg0[1][1]))) % 180
            clash = False
            for d1, seg1 in cands[1:]:
                if d1 - d0 > 6.0:
                    break
                axe1 = int(round(bearing(seg1[0][0], seg1[0][1], seg1[1][0], seg1[1][1]))) % 180
                diff = abs(axe1 - axe0) % 180
                if min(diff, 180 - diff) > 25 and (seg1[3] != seg0[3] or seg1[2] != seg0[2]):
                    clash = True
                    break
            if clash:
                ambiguous += 1
                continue
            r["axe"], r["cls"] = axe0, road_class(seg0[2])
            if not r["ref"]:
                r["ref"] = clean(seg0[3])
            found += 1
        time.sleep(1)
    print(f"Routes voisines : {found} radar(s) rattaché(s), {ambiguous} ambigu(s) laissé(s) sans orientation", flush=True)


def dedup(records):
    grid, out = {}, []
    for r in records:
        gx, gy = int(math.floor(r["lat"] * 1000)), int(math.floor(r["lon"] * 1000))
        dup = None
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for o in grid.get((gx + dx, gy + dy), ()):
                    if o["t"] == r["t"] and dist_m(o["lat"], o["lon"], r["lat"], r["lon"]) < DEDUP_METERS:
                        dup = o
                        break
                if dup:
                    break
            if dup:
                break
        if dup:
            # On complète la fiche gardée avec ce que l'autre sait en plus.
            for k in ("axe", "sens"):
                if dup[k] < 0 <= r[k]:
                    dup[k] = r[k]
            if not dup["cls"] and r["cls"]:
                dup["cls"] = r["cls"]
            if not dup["spd"] and r["spd"]:
                dup["spd"] = r["spd"]
            continue
        grid.setdefault((gx, gy), []).append(r)
        out.append(r)
    return out


def line_v1(r):
    return f'{r["t"]};{r["lat"]:.5f};{r["lon"]:.5f};{r["spd"]};{r["ref"]}'


def line_v2(r):
    end = f'{r["end"][0]:.5f};{r["end"][1]:.5f}' if r["end"] else ";"
    return f'{line_v1(r)};{r["axe"]};{r["sens"]};{r["cls"]};{end}'


def parse_existing(path, v2):
    recs = []
    try:
        for ln in open(path, encoding="utf-8"):
            ln = ln.rstrip("\n")
            if not ln or ln.startswith("#"):
                continue
            p = ln.split(";")
            if len(p) < 5:
                continue
            r = dict(t=p[0], lat=float(p[1]), lon=float(p[2]), spd=int(p[3] or 0), ref=p[4],
                     axe=-1, sens=-1, cls="", end=None)
            if v2 and len(p) >= 10:
                r["axe"], r["sens"], r["cls"] = int(p[5] or -1), int(p[6] or -1), p[7]
                if p[8] and p[9]:
                    r["end"] = (float(p[8]), float(p[9]))
            recs.append(r)
    except FileNotFoundError:
        pass
    return recs


def write(path, lines, note, fmt):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {note} — {len(lines)} radars — {fmt}\n")
        f.write("\n".join(lines))
        f.write("\n")


def write_meta(data_path, meta_path):
    rows = [ln.rstrip("\n") for ln in open(data_path, encoding="utf-8") if ln.strip() and not ln.startswith("#")]
    digest = hashlib.sha256("\n".join(rows).encode("utf-8")).hexdigest()
    try:
        old = json.load(open(meta_path, encoding="utf-8"))
    except Exception:
        old = {}
    if old.get("sha256") == digest:
        print(f"{os.path.basename(data_path)} : radars identiques, fiche inchangée")
        return False
    meta = {"version": max(int(time.strftime("%Y%m%d%H%M")), int(old.get("version", 0)) + 1),
            "date": time.strftime("%Y-%m-%d"),
            "count": len(rows), "sha256": digest}
    json.dump(meta, open(meta_path, "w", encoding="utf-8"), indent=2)
    print(f"{os.path.basename(meta_path)} : {meta}")
    return True


# ── MapAtlas Camera Index ───────────────────────────────────────────────────

def get_json(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": "VektraBuild/1.0 (BYD cockpit, offline radar base)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def in_europe(lat, lon):
    return LATS[0] <= lat <= LATS[-1] and LONS[0] <= lon <= LONS[-1]


def from_mapatlas(feature):
    """Radar MapAtlas, ou None (hors zone, classe inconnue, signalé hors service)."""
    geom = feature.get("geometry") or {}
    props = feature.get("properties") or {}
    if geom.get("type") != "Point":
        return None
    coords = geom.get("coordinates") or []
    if len(coords) < 2:
        return None
    lon, lat = float(coords[0]), float(coords[1])
    t = MAPATLAS_CLASS.get(str(props.get("class", "")))
    if t is None or not in_europe(lat, lon) or props.get("reportedInactive") is True:
        return None
    try:
        v = int(props.get("limitKph") or 0)
    except (TypeError, ValueError):
        v = 0
    spd = v if 20 <= v <= 140 else 0
    return dict(t=t, lat=lat, lon=lon, spd=spd, ref="", axe=-1, sens=-1, cls="", end=None)


def mapatlas_refresh(folder):
    """
    Met à jour radars/mapatlas_europe.txt seulement si MapAtlas a publié une nouvelle version.
    Au moindre pays en échec, l'ancien fichier est gardé tel quel (jamais de radars perdus).
    """
    cache = os.path.join(folder, "mapatlas_europe.txt")
    meta_path = os.path.join(folder, "mapatlas_meta.json")
    try:
        cat = get_json(MAPATLAS_URL + "catalog.json", 60)
    except Exception as ex:
        print(f"MapAtlas : catalogue inaccessible ({ex}), fichier gardé")
        return
    try:
        old = json.load(open(meta_path, encoding="utf-8"))
    except Exception:
        old = {}
    released = str(cat.get("released", ""))
    if old.get("released") == released and os.path.isfile(cache):
        print(f"MapAtlas : publication {released} déjà connue")
        return
    known = {str(r.get("code")) for r in cat.get("regions", [])}
    recs = []
    for code in MAPATLAS_CODES:
        if code not in known:
            continue
        try:
            data = get_json(MAPATLAS_URL + code + ".geojson")
        except Exception as ex:
            print(f"MapAtlas : {code} en échec ({ex}), fichier gardé")
            return
        n0 = len(recs)
        for f in data.get("features", []):
            r = from_mapatlas(f)
            if r:
                recs.append(r)
        print(f"  MapAtlas {code} -> {len(recs) - n0} radars", flush=True)
        time.sleep(0.5)
    recs = dedup(recs)
    if len(recs) < 1000:
        print(f"MapAtlas : résultat trop faible ({len(recs)}), fichier gardé")
        return
    with open(cache, "w", encoding="utf-8") as f:
        f.write(f"# MapAtlas Camera Index, publication {released}, relevé {cat.get('snapshot', '')}, "
                f"{cat.get('licence', '')}, {cat.get('attribution', '')} — {len(recs)} radars — TYPE;LAT;LON;VITESSE\n")
        f.write("\n".join(f'{r["t"]};{r["lat"]:.5f};{r["lon"]:.5f};{r["spd"]}' for r in recs))
        f.write("\n")
    json.dump({"released": released, "snapshot": cat.get("snapshot", ""), "licence": cat.get("licence", ""),
               "attribution": cat.get("attribution", ""), "count": len(recs)},
              open(meta_path, "w", encoding="utf-8"), indent=2)
    print(f"MapAtlas : {len(recs)} radars en Europe (publication {released})")


def parse_mapatlas(folder):
    recs = []
    try:
        for ln in open(os.path.join(folder, "mapatlas_europe.txt"), encoding="utf-8"):
            ln = ln.rstrip("\n")
            if not ln or ln.startswith("#"):
                continue
            p = ln.split(";")
            if len(p) < 4:
                continue
            recs.append(dict(t=p[0], lat=float(p[1]), lon=float(p[2]), spd=int(p[3] or 0), ref="",
                             axe=-1, sens=-1, cls="", end=None))
    except FileNotFoundError:
        pass
    return recs


def merge_sources(osm, atlas):
    """
    Fusion OSM + MapAtlas. Un radar MapAtlas du même type qu'un radar OSM à moins de 85 m est le
    même radar : la fiche OSM (plus riche) est gardée et marquée OA. Les autres restent A.
    """
    for r in osm:
        r["src"] = "O"
    grid = {}
    for r in osm:
        grid.setdefault((int(math.floor(r["lat"] * 1000)), int(math.floor(r["lon"] * 1000))), []).append(r)
    added = []
    for a in atlas:
        gx, gy = int(math.floor(a["lat"] * 1000)), int(math.floor(a["lon"] * 1000))
        twin = None
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for o in grid.get((gx + dx, gy + dy), ()):
                    if o["t"] == a["t"] and dist_m(o["lat"], o["lon"], a["lat"], a["lon"]) < DEDUP_METERS:
                        twin = o
                        break
                if twin:
                    break
            if twin:
                break
        if twin:
            twin["src"] = "OA"
        else:
            a["src"] = "A"
            added.append(a)
    return osm + added


def write_v3(folder):
    """radars_v3.txt : base OSM (radars_v2.txt) + MapAtlas, avec la source de chaque radar."""
    v2_path = os.path.join(folder, "radars_v2.txt")
    v3_path = os.path.join(folder, "radars_v3.txt")
    osm = parse_existing(v2_path, True)
    if len(osm) < MIN_RADARS:
        print("Format 3 : base OSM absente ou trop faible, fichier inchangé")
        return
    try:
        osm_note = open(v2_path, encoding="utf-8").readline().lstrip("# ").split(" — ")[0].strip()
    except Exception:
        osm_note = "OpenStreetMap Europe"
    atlas = parse_mapatlas(folder)
    try:
        am = json.load(open(os.path.join(folder, "mapatlas_meta.json"), encoding="utf-8"))
    except Exception:
        am = {}
    merged = merge_sources(osm, atlas)
    both = sum(1 for r in merged if r["src"] == "OA")
    only_a = sum(1 for r in merged if r["src"] == "A")
    note = (f"{osm_note} + MapAtlas Camera Index (relevé {am.get('snapshot', '?')}, CC BY 4.0, mapatlas.eu)")
    write(v3_path, [line_v2(r) + ";" + r["src"] for r in merged], note,
          "TYPE;LAT;LON;VITESSE;ROUTE;AXE;SENS;CLASSE;FIN_LAT;FIN_LON;SOURCE")
    print(f"Format 3 : {len(osm)} radars OSM (dont {both} aussi dans MapAtlas) + {only_a} radars MapAtlas seuls")
    write_meta(v3_path, os.path.join(folder, "radars_v3_meta.json"))


def weekly(folder):
    v1_path = os.path.join(folder, "radars_europe.txt")
    v2_path = os.path.join(folder, "radars_v2.txt")
    records, failed = [], 0

    # 1. Relations : sens de circulation fiable et début / fin des tronçons.
    rels = http(q_relations("(34,-25,72,45)", 180), "relations Europe", 180)
    if rels is None:
        rels = []
        for b in tiles():
            part = http(q_relations(b, 120), f"relations {b}", 120)
            if part is None:
                failed += 1
                FAILED_BOXES.append(b)
            else:
                rels.extend(part)
    for rel in rels:
        if rel.get("type") == "relation":
            r = from_relation(rel)
            if r:
                records.append(r)

    # 2. Radars (nœuds) avec les routes qui les portent ; zone lourde découpée, repli sans les routes.
    for b in tiles():
        if not fetch_nodes(b, 10.0, records):
            failed += 1

    roads_near_off_road(records)
    fresh = dedup(records)
    print(f"Téléchargé : {len(fresh)} radars après tri, {failed} requête(s) en échec")

    # 3. Radars connus situés dans une zone qui n'a pas pu être téléchargée : conservés.
    #    Ailleurs, la base suit OpenStreetMap : un radar supprimé là-bas disparaît aussi ici.
    known = parse_existing(v2_path, True) or parse_existing(v1_path, False)
    known = [r for r in known if any(in_box(r, b) for b in FAILED_BOXES)]
    merged = dedup(fresh + known)
    kept = len(merged) - len(fresh)
    print(f"Base existante : {kept} radar(s) absent(s) du téléchargement conservé(s)")

    if len(merged) < MIN_RADARS:
        print("Résultat trop faible : fichiers inchangés.")
        mapatlas_refresh(folder)
        write_v3(folder)
        return
    note = f"OpenStreetMap Europe, {time.strftime('%Y-%m-%d')}, {failed} requête(s) en échec"
    write(v1_path, [line_v1(r) for r in merged], note, "TYPE;LAT;LON;VITESSE;ROUTE")
    write(v2_path, [line_v2(r) for r in merged], note,
          "TYPE;LAT;LON;VITESSE;ROUTE;AXE;SENS;CLASSE;FIN_LAT;FIN_LON")
    with_axis = sum(1 for r in merged if r["axe"] >= 0)
    with_dir = sum(1 for r in merged if r["sens"] >= 0)
    sections = sum(1 for r in merged if r["t"] == "S")
    with_end = sum(1 for r in merged if r["end"])
    print(f"Avec orientation de route : {with_axis} ; avec sens contrôlé : {with_dir} ; "
          f"tronçons : {sections} dont {with_end} avec début et fin")
    write_meta(v1_path, os.path.join(folder, "radars_meta.json"))
    write_meta(v2_path, os.path.join(folder, "radars_v2_meta.json"))
    # Format 3 : la même base OSM, plus MapAtlas.
    mapatlas_refresh(folder)
    write_v3(folder)


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "weekly":
        weekly(sys.argv[2])
        return
    if len(sys.argv) >= 3 and sys.argv[1] == "v3":
        mapatlas_refresh(sys.argv[2])
        write_v3(sys.argv[2])
        return
    if len(sys.argv) >= 4 and sys.argv[1] == "meta":
        write_meta(sys.argv[2], sys.argv[3])
        return
    print(__doc__)
    sys.exit(2)


if __name__ == "__main__":
    main()
