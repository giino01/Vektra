#!/usr/bin/env python3
"""
Base de radars embarquée dans l'APK : tous les radars connus d'OpenStreetMap pour l'Europe.

Le runner GitHub (qui a internet) interroge Overpass tuile par tuile, classe chaque radar
EXACTEMENT comme l'application (voir VektraRoadRadarTrafficEngine.parseOverpassElements),
supprime les doublons et écrit un fichier compact, une ligne par radar :

    TYPE;LAT;LON;VITESSE;ROUTE

TYPE : F = fixe, S = tronçon, R = feu rouge, M = mobile. VITESSE = 0 si inconnue.

Usage :
    build_radars.py fetch  <sortie.txt>               # Europe entière depuis Overpass
    build_radars.py meta   <base.txt> <meta.json>     # fiche de version lue par l'application
    build_radars.py convert <overpass.json> <sortie.txt>  # conversion d'un fichier Overpass existant

Le fichier n'est remplacé que si le résultat dépasse MIN_RADARS : en cas de panne des
serveurs, la base déjà commitée est conservée et le build continue.
"""
import json
import sys
import time
import urllib.parse
import urllib.request

# Ordre constaté sur les builds : overpass-api.de répond le plus vite ; kumi.systems dépassait
# souvent le délai, il passe en dernier.
ENDPOINTS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.openstreetmap.fr/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
]

# Europe : latitudes 34 → 72, longitudes -25 → 45, en tuiles de 10° × 10°.
LATS = [34, 44, 54, 64, 72]
LONS = [-25, -15, -5, 5, 15, 25, 35, 45]

MIN_RADARS = 5000
DEDUP_METERS = 85.0


# Deux requêtes légères plutôt qu'une lourde : les radars (nœuds) d'un côté, les relations
# « enforcement » (tronçons, feux rouges) de l'autre. Les nœuds ou chemins portant directement
# « enforcement » ne sont pas standard dans OpenStreetMap et rendaient la requête très lente.
def node_query(b, timeout):
    return (f"[out:json][timeout:{timeout}];("
            f'node["highway"="speed_camera"]{b};'
            f'node["highway"="speed_display"]["speed_camera"]{b};'
            ");out qt;")


def relation_query(b, timeout):
    return f'[out:json][timeout:{timeout}];relation["enforcement"]{b};out center tags qt;'


import os
# Temps maximal de téléchargement (minutes) : RADARS_MINUTES, 22 par défaut.
DEADLINE = time.time() + float(os.environ.get("RADARS_MINUTES", "22")) * 60


def run(query, label, http_timeout):
    data = urllib.parse.urlencode({"data": query}).encode()
    for ep in ENDPOINTS:
        if time.time() > DEADLINE:
            print(f"  {label} : temps écoulé, abandon", flush=True)
            return None
        try:
            req = urllib.request.Request(ep, data=data, headers={
                "User-Agent": "VektraBuild/1.0 (BYD cockpit, offline radar base)",
                "Referer": "https://overpass-turbo.eu/",
            })
            with urllib.request.urlopen(req, timeout=http_timeout) as r:
                body = json.loads(r.read().decode("utf-8"))
            if "remark" in body and "runtime error" in str(body.get("remark", "")):
                raise RuntimeError(body["remark"])
            els = body.get("elements", [])
            print(f"  {label} -> {len(els)} éléments ({ep})", flush=True)
            return els
        except Exception as ex:  # serveur occupé, délai dépassé…
            print(f"  {label} : échec {ep} ({ex})", flush=True)
            time.sleep(5)
    return None


def fetch_kind(make_query, kind, whole_first):
    """Tuile par tuile (10° × 10°) ; pour les relations, peu nombreuses, l'Europe d'abord d'un seul coup."""
    if whole_first:
        els = run(make_query("(34,-25,72,45)", 180), f"{kind} Europe", 200)
        if els is not None:
            return els, 0
    all_els, failed = [], 0
    for i in range(len(LATS) - 1):
        for j in range(len(LONS) - 1):
            b = f"({LATS[i]},{LONS[j]},{LATS[i + 1]},{LONS[j + 1]})"
            part = run(make_query(b, 120), f"{kind} {b}", 140)
            if part is None:
                failed += 1
            else:
                all_els.extend(part)
            time.sleep(1)
    return all_els, failed


def classify(tags):
    """Copie fidèle du classement de l'application. Renvoie F/S/R/M, W (chantier) ou None."""
    g = lambda k: str(tags.get(k, "")).lower()
    highway, enforcement, construction = g("highway"), g("enforcement"), g("construction")
    cam_type, cam_mount, speed_cam = g("camera:type"), g("camera:mount"), g("speed_camera")
    text = (g("name") + " " + g("description") + " " + g("note"))
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
    if (highway == "speed_camera" or enforcement in ("maxspeed", "speed")
            or cam_type in ("fixed", "speed")):
        return "F"
    return None


def max_speed(tags):
    digits = "".join(c for c in str(tags.get("maxspeed", "")) if c.isdigit())
    try:
        v = int(digits) if digits else 0
    except ValueError:
        v = 0
    return v if 20 <= v <= 140 else 0


def compact(elements):
    import math
    seen_ids = set()
    grid = {}
    out = []
    for el in elements:
        key = (el.get("type"), el.get("id"))
        if key in seen_ids:
            continue
        seen_ids.add(key)
        tags = el.get("tags") or {}
        if not tags:
            continue
        if el.get("type") == "node":
            lat, lon = el.get("lat"), el.get("lon")
        else:
            c = el.get("center") or {}
            lat, lon = c.get("lat"), c.get("lon")
        if lat is None or lon is None:
            continue
        t = classify(tags)
        if t is None or t == "W":
            continue
        # Doublons : même type à moins de 85 m (grille de ~110 m, cases voisines comprises).
        gx, gy = int(math.floor(lat * 1000)), int(math.floor(lon * 1000))
        dup = False
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for (t2, la2, lo2) in grid.get((gx + dx, gy + dy), ()):
                    if t2 != t:
                        continue
                    dlat = math.radians(la2 - lat)
                    dlon = math.radians(lo2 - lon)
                    a = (math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat)) *
                         math.cos(math.radians(la2)) * math.sin(dlon / 2) ** 2)
                    if 6371000.0 * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) < DEDUP_METERS:
                        dup = True
                        break
                if dup:
                    break
            if dup:
                break
        if dup:
            continue
        grid.setdefault((gx, gy), []).append((t, lat, lon))
        ref = str(tags.get("ref", "") or tags.get("name", "")).replace(";", ",").replace("\n", " ").strip()[:40]
        out.append(f"{t};{lat:.5f};{lon:.5f};{max_speed(tags)};{ref}")
    return out


def write(lines, path, note):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {note} — {len(lines)} radars — TYPE;LAT;LON;VITESSE;ROUTE\n")
        f.write("\n".join(lines))
        f.write("\n")


def main():
    if len(sys.argv) >= 4 and sys.argv[1] == "convert":
        els = json.load(open(sys.argv[2], encoding="utf-8")).get("elements", [])
        lines = compact(els)
        write(lines, sys.argv[3], "OpenStreetMap (conversion)")
        print(f"Converti : {len(lines)} radars")
        return
    if len(sys.argv) >= 3 and sys.argv[1] == "fetch":
        out_path = sys.argv[2]
        rels, f2 = fetch_kind(relation_query, "tronçons et feux", True)
        nodes, f1 = fetch_kind(node_query, "radars", False)
        all_els, failed = nodes + rels, f1 + f2
        lines = compact(all_els)
        # Les radars de la base déjà commitée sont gardés s'ils manquent (tuile en échec) :
        # une panne de serveur ne doit jamais faire disparaître des radars connus.
        try:
            import math
            have = {}
            for ln in lines:
                t, la, lo = ln.split(";")[:3]
                have.setdefault((t, round(float(la), 3), round(float(lo), 3)), True)
            kept = 0
            for ln in open(out_path, encoding="utf-8"):
                ln = ln.strip()
                if not ln or ln.startswith("#"):
                    continue
                t, la, lo = ln.split(";")[:3]
                la, lo = float(la), float(lo)
                near = any((t, round(la + dx, 3), round(lo + dy, 3)) in have
                           for dx in (-0.001, 0, 0.001) for dy in (-0.001, 0, 0.001))
                if not near:
                    lines.append(ln)
                    kept += 1
            print(f"Base commitée : {kept} radar(s) absent(s) du téléchargement conservé(s)")
        except Exception as ex:
            print(f"Base commitée illisible ({ex})")
        print(f"Europe : {len(all_els)} éléments, {len(lines)} radars après tri, {failed} tuile(s) en échec")
        if len(lines) >= MIN_RADARS:
            write(lines, out_path, f"OpenStreetMap Europe, {time.strftime('%Y-%m-%d')}, {failed} tuile(s) manquante(s)")
            print(f"Base Europe écrite : {out_path}")
        else:
            print("Résultat trop faible : base déjà commitée conservée.")
        return
    if len(sys.argv) >= 4 and sys.argv[1] == "meta":
        # Fiche lue par l'application : la version ne change que si les radars ont changé.
        import hashlib
        data_path, meta_path = sys.argv[2], sys.argv[3]
        rows = [ln.rstrip("\n") for ln in open(data_path, encoding="utf-8") if ln.strip() and not ln.startswith("#")]
        digest = hashlib.sha256("\n".join(rows).encode("utf-8")).hexdigest()
        try:
            old = json.load(open(meta_path, encoding="utf-8"))
        except Exception:
            old = {}
        if old.get("sha256") == digest:
            print("Radars identiques : fiche inchangée")
            print("UNCHANGED")
            return
        meta = {
            "version": int(time.strftime("%Y%m%d%H")),
            "date": time.strftime("%Y-%m-%d"),
            "count": len(rows),
            "sha256": digest,
        }
        json.dump(meta, open(meta_path, "w", encoding="utf-8"), indent=2)
        print(f"Fiche : {meta}")
        return
    print(__doc__)
    sys.exit(2)


if __name__ == "__main__":
    main()
