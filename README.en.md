<div align="center">

# V E K T R A

**Your BYD cluster, your way.**

Custom dashboard for the screen behind the steering wheel on BYD DiLink 3 vehicles.

**VERSION 1.8.10** · released on 26 October 2026 · 43.0 MB

[**Download the app**](https://giino01.github.io/Vektra/Vektra-1.8.10.apk) · [**Project page**](https://giino01.github.io/Vektra/)

[Français](README.md) · **English** · [Italiano](README.it.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Türkçe](README.tr.md)

</div>

---

## Overview

![The cluster in blue mood](img/combine-normal.png)

From left to right: the date, the **needle speedometer** graduated to 220 km/h, the **track playing** whatever app is playing it, three figures chosen by mode, the **energy flow line** whose centre dot moves right in red as the battery drains and left in green as it charges, then the **animated weather** and the **pressure of all four tyres** in bar.

![The cluster in red mood, Sport mode](img/combine-sport.png)

In Sport the mood turns red, a `SPORT` badge appears and the three bottom figures change: power, engine speed and accelerator position, instead of consumption and battery.

> The screenshots on this page are **drawn by the code of the published version** at every release, with demo values. They cannot show a version older than the one offered here.

## Themes

The **Theme** key opens the **Theme Store** and cycles through the installed themes. **Carbone 3D** is the built-in default and **VektraUI** the other built-in theme; the **Aston** theme downloads in one tap. The choice is remembered and comes back at the next start.

![The same theme on a light background](img/clair-theme-hyperos3d.png)

Every theme exists in dark and light. The light background picks up the blue-grey of the BYD overlay, measured from photographs, so the app blends into it instead of sitting on top. The **Appearance** setting picks one, the other, or follows the tablet.

## What you need

- A **BYD with DiLink 3** (Android 10). Developed on a Seal U DM-i; other DiLink 3 models have not been verified.
- The tablet must accept **installing outside applications** (sideload).
- **Network ADB debugging** active on the tablet, port 5555. VEKTRA connects to it locally, on the tablet itself — nothing leaves the vehicle.
- An internet connection on the tablet for weather and updates. Everything else works offline.

**Why ADB.** The commands that free the cluster screen are allowed only to Android's `shell` user. An ordinary application cannot send them. VEKTRA therefore goes through the tablet's own ADB, locally, to obtain that right.

## Installation

1. Download the application file from this page, on the tablet.
2. Open it and accept the installation. If Android refuses, allow "unknown sources" for the file manager you used.
3. Open VEKTRA. On the very first start, the welcome screen asks for the language.
4. Press **Continue**. The main screen opens.
5. The first command sent will raise the prompt **"Allow USB debugging?"**. Tick **Always allow**, then accept. This prompt appears only once.

![Welcome screen and language choice](img/accueil-langue.png)

Six languages are available: French, English, Italian, German, Brazilian Portuguese and Turkish.

## Turning the display on

1. In the **Control** section, press **Check · ADB and diagnostics**. This is what triggers the debugging prompt and confirms the connection works.
2. Go back to **Cluster** and press **Show on the cluster**.
3. The stock dashboard goes to sleep, the virtual cluster display is created, then VEKTRA appears on it. It takes about ten seconds.
4. The preview in the middle of the tablet shows live what is drawn behind the wheel. The **Preview** button folds it away if you prefer a status board.

**To go back**, press **Restore the original**: the BYD dashboard takes over again. If it does not come back, switch the ignition off and on.

## The four sections

| Section | What it is for |
| --- | --- |
| **Cluster** | The live preview, the display button, the choice of screen, mode and theme. |
| **Control** | The full report of detected equipment, with a button to copy it all. |
| **Log** | Every command sent and every answer received. |
| **Settings** | Language, appearance, auto start, music access, updates, weather. |

![Cluster](img/tablette-combine.png)

![Settings](img/tablette-reglages.png)

## Music

To show the track playing, VEKTRA needs **notification access**: that is Android's rule for reading audio sessions. Press the **Notification access** row and the app grants it to itself over ADB, without erasing anything from the existing list. Once granted, the title, artist, cover art and progress appear, **whatever app is playing** — radio, Bluetooth, or an installed app.

## Automatic start and stop

With this setting on, VEKTRA takes the cluster as soon as the car is switched on and hands it back as soon as it is switched off. The vehicle state is read **directly from the car**, once a second: 0 off, 1 accessories, 2 ignition on. A shutdown must be confirmed twice in a row before the screen is handed back — a single hiccup must not make the display vanish mid-road.

## Appearance

Dark, light, or automatic — the appearance then follows the tablet. The setting applies to the cluster only: the tablet screen stays dark at all times, it is a cockpit.

## Update

VEKTRA checks by itself at every opening. When a version is available, a window shows the news and offers **Later** or **Download and install**. If you accept, the app downloads itself, installs over the old one and reopens on its own. Every version carries the **same signature**: an update always replaces the previous one without Android refusing it, and without losing the settings.

## If something goes wrong

- **The cluster stays frozen.** Press *Restore the original*, then try again. If nothing changes, switch the ignition off and on.
- **No data, only dashes.** The car SDK did not answer. The Control section says which devices can be reached.
- **Music does not show.** Notification access has not been granted: see above. Also check that something is actually playing.
- **The update says "Unavailable".** The tablet could not reach the source. Check its internet connection, then try again: the exact reason is shown.
- **Anything else.** Open *Control*, press *Copy the whole scan*, then send the text. It contains everything needed to understand.

## What is new in 1.8.10

- "Control" scan: the BYD data list is reordered (most useful devices last) and trimmed (permissions and technical lists removed), so copy-paste no longer cuts off the first devices. Helps find the real data names for the Info widget.

---

Personal project, with no connection to BYD. Install and use at your own risk. The information shown comes from the car's system and may be inaccurate: never rely on it to drive.
