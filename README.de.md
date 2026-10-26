<div align="center">

# V E K T R A

**Das Kombiinstrument deines BYD, nach deinem Geschmack.**

Individuelles Kombiinstrument für den Bildschirm hinter dem Lenkrad von BYD-DiLink-3-Fahrzeugen.

**VERSION 1.8.1** · veröffentlicht am 26. Oktober 2026 · 43.0 MB

[**Anwendung herunterladen**](https://giino01.github.io/Vektra/Vektra-1.8.1.apk) · [**Projektseite**](https://giino01.github.io/Vektra/)

[Français](README.md) · [English](README.en.md) · [Italiano](README.it.md) · **Deutsch** · [Português](README.pt.md) · [Türkçe](README.tr.md)

</div>

---

## Überblick

![Das Kombi in blauer Stimmung](img/combine-normal.png)

Von links nach rechts: das Datum, der **Zeigertacho** mit Skala bis 220 km/h, der **laufende Titel** aus jeder beliebigen App, drei je nach Modus gewählte Werte, die **Energieflusslinie**, deren Mittelpunkt beim Entladen rot nach rechts und beim Laden grün nach links wandert, dann das **animierte Wetter** und der **Druck aller vier Reifen** in bar.

![Das Kombi in roter Stimmung, Sport-Modus](img/combine-sport.png)

Im Sport-Modus wird die Stimmung rot, ein `SPORT`-Abzeichen erscheint und die drei unteren Werte ändern sich: Leistung, Drehzahl und Gaspedalstellung statt Verbrauch und Batterie.

> Die Bilder auf dieser Seite werden bei jeder Veröffentlichung **vom Code der veröffentlichten Version gezeichnet**, mit Beispielwerten. Sie können also keine ältere Version zeigen als die hier angebotene.

## Acht Themen

Die Taste **Thema** blättert durch acht Anordnungen: Carbon, Carbon 3D, Grand Tourer, Energiefluss, Obsidian, Rot Sport, Lumen und Nebula. Ein Druck wechselt zur nächsten. Die Wahl wird gemerkt und kehrt beim nächsten Start zurück.

![Dasselbe Thema auf hellem Hintergrund](img/clair-theme-hyperos3d.png)

Jedes Thema gibt es dunkel und hell. Der helle Hintergrund nimmt das Blaugrau der BYD-Oberfläche auf, auf Fotos ausgemessen, damit die App darin verschmilzt statt darauf zu liegen. Die Einstellung **Erscheinungsbild** wählt das eine, das andere, oder folgt dem Tablet.

## Was nötig ist

- Ein **BYD mit DiLink 3** (Android 10). Entwickelt auf einem Seal U DM-i; andere DiLink-3-Modelle wurden nicht geprüft.
- Das Tablet muss die **Installation fremder Anwendungen** zulassen (Sideload).
- **ADB-Debugging über Netzwerk** auf dem Tablet aktiv, Port 5555. VEKTRA verbindet sich lokal auf dem Tablet selbst — nichts verlässt das Fahrzeug.
- Eine Internetverbindung auf dem Tablet für Wetter und Aktualisierungen. Alles andere läuft offline.

**Warum ADB.** Die Befehle, die den Kombi-Bildschirm freigeben, sind nur dem `shell`-Benutzer von Android erlaubt. Eine gewöhnliche Anwendung kann sie nicht senden. VEKTRA geht deshalb lokal über das ADB des Tablets, um dieses Recht zu erhalten.

## Installation

1. Lade die Anwendungsdatei von dieser Seite auf das Tablet.
2. Öffne sie und bestätige die Installation. Lehnt Android ab, erlaube „unbekannte Quellen" für den verwendeten Dateimanager.
3. Öffne VEKTRA. Beim allerersten Start fragt der Startbildschirm nach der Sprache.
4. Tippe auf **Weiter**. Der Hauptbildschirm öffnet sich.
5. Beim ersten gesendeten Befehl erscheint die Abfrage **„USB-Debugging zulassen?"**. Setze das Häkchen bei **Immer zulassen** und bestätige. Sie erscheint nur einmal.

![Startbildschirm und Sprachwahl](img/accueil-langue.png)

Sechs Sprachen stehen zur Verfügung: Französisch, Englisch, Italienisch, Deutsch, brasilianisches Portugiesisch und Türkisch.

## Anzeige einschalten

1. Tippe im Bereich **Kontrolle** auf **Prüfen · ADB und Diagnose**. Das löst die Debugging-Abfrage aus und bestätigt, dass die Verbindung steht.
2. Gehe zurück zu **Kombiinstrument** und tippe auf **Auf dem Kombi anzeigen**.
3. Die Serienanzeige geht in den Ruhezustand, der virtuelle Kombi-Bildschirm wird erzeugt, dann erscheint VEKTRA darauf. Das dauert etwa zehn Sekunden.
4. Die Vorschau in der Mitte des Tablets zeigt live, was hinter dem Lenkrad gezeichnet wird. Die Taste **Vorschau** klappt sie zu, wenn du lieber eine Statusübersicht hast.

**Zum Zurückgehen** tippe auf **Original wiederherstellen**: die BYD-Anzeige übernimmt wieder. Kehrt sie nicht zurück, Zündung aus- und wieder einschalten.

## Die vier Bereiche

| Bereich | Wofür er da ist |
| --- | --- |
| **Kombiinstrument** | Die Live-Vorschau, die Anzeigetaste, die Wahl von Bildschirm, Modus und Thema. |
| **Kontrolle** | Der vollständige Bericht der erkannten Geräte, mit einer Taste zum Kopieren. |
| **Protokoll** | Jeder gesendete Befehl und jede empfangene Antwort. |
| **Einstellungen** | Sprache, Erscheinungsbild, Autostart, Musikzugriff, Aktualisierungen, Wetter. |

![Kombiinstrument](img/tablette-combine.png)

![Einstellungen](img/tablette-reglages.png)

## Musik

Um den laufenden Titel anzuzeigen, braucht VEKTRA den **Benachrichtigungszugriff**: so verlangt es Android zum Lesen der Audiositzungen. Tippe auf die Zeile **Benachrichtigungszugriff**, und die App erteilt ihn sich selbst über ADB, ohne etwas aus der bestehenden Liste zu löschen. Danach erscheinen Titel, Interpret, Cover und Fortschritt, **egal welche App spielt** — Radio, Bluetooth oder eine installierte App.

## Automatisches Starten und Beenden

Ist diese Einstellung aktiv, übernimmt VEKTRA das Kombi, sobald das Auto eingeschaltet wird, und gibt es frei, sobald es ausgeschaltet wird. Der Fahrzeugzustand wird **direkt im Auto** gelesen, einmal pro Sekunde: 0 aus, 1 Zubehör, 2 Zündung an. Ein Abschalten muss zweimal hintereinander bestätigt werden, bevor der Bildschirm freigegeben wird — ein einzelner Aussetzer darf die Anzeige nicht während der Fahrt verschwinden lassen.

## Erscheinungsbild

Dunkel, hell oder automatisch — das Erscheinungsbild folgt dann dem Tablet. Die Einstellung betrifft nur das Kombi: der Tablet-Bildschirm bleibt immer dunkel, er ist ein Cockpit.

## Aktualisierung

VEKTRA prüft bei jedem Öffnen selbst. Ist eine Version verfügbar, zeigt ein Fenster die Neuerungen und bietet **Später** oder **Herunterladen und installieren**. Bei Zustimmung lädt sich die App herunter, installiert sich darüber und öffnet sich wieder. Alle Versionen tragen die **gleiche Signatur**: eine Aktualisierung ersetzt die vorherige immer, ohne dass Android sie ablehnt, und ohne die Einstellungen zu verlieren.

## Wenn etwas klemmt

- **Das Kombi bleibt eingefroren.** Tippe auf *Original wiederherstellen* und versuche es erneut. Ändert sich nichts, Zündung aus- und wieder einschalten.
- **Keine Daten, nur Striche.** Das Fahrzeug-SDK hat nicht geantwortet. Der Bereich Kontrolle zeigt, welche Geräte erreichbar sind.
- **Die Musik erscheint nicht.** Der Benachrichtigungszugriff wurde nicht erteilt: siehe oben. Prüfe auch, ob wirklich etwas spielt.
- **Die Aktualisierung meldet „Nicht verfügbar".** Das Tablet hat die Quelle nicht erreicht. Prüfe die Internetverbindung und versuche es erneut: der genaue Grund wird angezeigt.
- **Etwas anderes.** Öffne *Kontrolle*, tippe auf *Ganzen Scan kopieren* und sende den Text. Er enthält alles Nötige zum Verstehen.

## Neu in 1.8.1

- Theme Store: neuer Bereich im linken Menü, auch über die Taste „Thema“ erreichbar. Karbon 3D bleibt das integrierte Standardthema; das Thema Aston lässt sich mit einem Tippen herunterladen, mit Vorschau, Größe, Fortschritt, Anwenden, Aktualisieren und Entfernen. Jedes Thema wird vor der Installation geprüft (Vektra-Signatur); eine anders erhaltene .vektra-Datei lässt sich auch über „Thema importieren“ installieren. Kommende Themen kommen auf demselben Weg.
- Vektra-3D-Karte: eine flüssige Karte, direkt vom Tablet gezeichnet, mit 3D-Gebäuden, die dem Auto ständig folgt. Sie ist jetzt die Karte aller Bildschirme: Reiter „Navigation“, Navigations-Widget von Karbon 3D, Aston-Thema und Karte im ganzen Kombi; der Pfeil bleibt auf der befahrenen Straße und die blaue Linie beginnt am Pfeil (der gefahrene Teil verschwindet). Neuer Bereich „Karte“ in den Einstellungen: Stil, 3D-Gebäude und Zoom.
- Aston-Thema (im Theme Store): zwei Anzeigen, Fahrstufe P R N D, Warnleuchten und in der Mitte Musik, Wetter oder Karte; eine auf dem Tablet gestartete Route erscheint im Kombiinstrument (nächste Abbiegung, Entfernung, Restzeit, Ankunftszeit, echte Blitzer).
- Navigation: die Führung folgt dem Auto jetzt entlang der Route. Die nächste Anweisung rückt während der Fahrt vor, Restentfernung und Restzeit werden auf der Route gemessen, jedes Manöver wird angesagt und die Ankunft gemeldet. Die Route wird automatisch neu berechnet, wenn man sie verlässt oder in falscher Richtung fährt, in Fahrtrichtung des Autos. Die Karte wird nicht mehr bei jeder GPS-Position langsamer.
- Keine erfundenen Werte mehr: ohne Fahrzeugdaten zeigen die Bildschirme „--“ statt einer Demo-Geschwindigkeit, -Batterie, eines Reifendrucks, Tempolimits oder Titels; keine falschen Blitzer mehr auf der Route oder als Ansage; Fahrstufe M oder S wird nicht mehr als „D“ angezeigt.
- Import von Widgets und Themen: Lesen im Hintergrund (eine große Datei friert den Bildschirm nicht mehr ein), Größe begrenzt, Bilder auf Kombigröße verkleinert; die tatsächlich unterstützten Formate werden genannt (Bilder, Vektra-Widget .json, Anordnung .json, .zip, .vektra); ein KWGT-, SVG-, HTML- oder XML-Widget wird mit Erklärung abgelehnt.
- Bearbeiten: ein ausgeblendetes oder nicht importiertes Widget fängt keine Berührungen mehr ab, das große Navigations-Widget behält die Auswahl nicht mehr, der Gesamtzoom wird nicht mehr doppelt auf die Kartenränder angewendet, und die Tablet-Vorschau hat kein Loch mehr anstelle der Karte.
- Oberfläche: alle Fenster (Stimme, Sprache der Stimme, Import, Variablen, Update-Quelle, Spende) und alle Meldungen im Stil der App; die Tastatur öffnet sich im Adressfeld.
- Anzeige im Kombiinstrument: die vollständige VEKTRA-Anzeige kehrt von selbst zurück, wenn der Autostart die App neu startet (sie konnte schwarz bleiben), und die Karte verschwindet nach einem Neustart nicht mehr; VektraUI wird jetzt sauber dargestellt, ohne Karbon-3D-Elemente darüber.

---

Privates Projekt, ohne jede Verbindung zu BYD. Installation und Nutzung auf eigene Gefahr. Die angezeigten Angaben stammen aus dem Fahrzeugsystem und können falsch sein: verlasse dich beim Fahren nie darauf.
