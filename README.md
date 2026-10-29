<div align="center">

# V E K T R A

**Le combiné de ta BYD, à ta façon.**

Tableau de bord personnalisé pour l'écran derrière le volant des véhicules BYD DiLink 3.

**VERSION 2.0.2** · publiée le 29 octobre 2026 · 45.9 Mo

[**Télécharger l'application**](https://giino01.github.io/Vektra/Vektra-2.0.2.apk) · [**Page du projet**](https://giino01.github.io/Vektra/)

**Français** · [English](README.en.md) · [Italiano](README.it.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Türkçe](README.tr.md)

</div>

---

## Aperçu

![Le combiné en ambiance bleue](img/combine-normal.png)

De gauche à droite : la date, le **compteur à aiguille** gradué jusqu'à 220 km/h, la **musique en cours** quelle que soit l'application qui la joue, trois chiffres choisis selon le mode, la **ligne de flux d'énergie** dont le point central part vers la droite en rouge quand la batterie se décharge et vers la gauche en vert quand elle se recharge, puis la **météo animée** et la **pression des quatre pneus** en bar.

![Le combiné en ambiance rouge, mode Sport](img/combine-sport.png)

En Sport, l'ambiance passe au rouge, une pastille `SPORT` apparaît et les trois chiffres du bas changent : puissance, régime moteur et position de l'accélérateur, à la place des consommations et de la batterie.

> Les captures de cette page sont **dessinées par le code de la version publiée** à chaque publication, avec des valeurs de démonstration. Elles ne peuvent donc pas montrer une version plus ancienne que celle proposée ici.

## Les thèmes

La touche **Thème** ouvre le **Theme Store** et fait défiler les thèmes installés. **Carbone 3D** est le thème intégré par défaut et **VektraUI** l'autre thème intégré ; le thème **Aston** se télécharge en un geste. Le choix est retenu et revient à l'allumage.

![Le même thème en fond clair](img/clair-theme-hyperos3d.png)

Chaque thème existe en sombre et en clair. Le fond clair reprend le bleu-gris de la surcouche BYD, mesuré sur photo, pour que l'application se fonde dedans au lieu d'y être posée. Le réglage **Apparence** choisit l'un, l'autre, ou suit la tablette.

## Ce qu'il faut

- Un véhicule **BYD équipé de DiLink 3** (Android 10). Mis au point sur une Seal U DM-i ; les autres modèles DiLink 3 n'ont pas été vérifiés.
- La tablette doit accepter l'**installation d'applications extérieures** (sideload).
- Le **débogage ADB en réseau** actif sur la tablette, port 5555. VEKTRA s'y connecte en local, sur la tablette elle-même — rien ne sort du véhicule.
- Une connexion internet sur la tablette pour la météo et les mises à jour. Tout le reste fonctionne hors ligne.

**Pourquoi l'ADB.** Les commandes qui libèrent l'écran du combiné ne sont autorisées qu'à l'utilisateur `shell` d'Android. Une application ordinaire ne peut pas les envoyer. VEKTRA passe donc par l'ADB de la tablette, en local, pour obtenir ce droit.

## Installation

1. Télécharge le fichier de l'application depuis cette page, sur la tablette.
2. Ouvre-le et accepte l'installation. Si Android refuse, autorise les « sources inconnues » pour le gestionnaire de fichiers utilisé.
3. Ouvre VEKTRA. Au tout premier démarrage, l'écran d'accueil demande la langue.
4. Appuie sur **Continuer**. L'écran principal s'ouvre.
5. La première commande envoyée fera apparaître la demande **« Autoriser le débogage USB ? »**. Coche **Toujours autoriser**, puis accepte. Cette demande n'apparaît qu'une fois.

![Écran d'accueil et choix de la langue](img/accueil-langue.png)

Six langues sont disponibles : français, anglais, italien, allemand, portugais du Brésil et turc.

## Activer l'affichage

1. Dans la section **Contrôle**, appuie sur **Vérifier · ADB et diagnostic**. C'est ce qui déclenche l'autorisation de débogage et confirme que la connexion fonctionne.
2. Reviens sur **Combiné** et appuie sur **Afficher sur le combiné**.
3. Le tableau de bord d'origine se met en veille, l'écran virtuel du combiné est créé, puis VEKTRA s'y affiche. L'opération prend une dizaine de secondes.
4. L'aperçu au centre de la tablette montre en direct ce qui est dessiné derrière le volant. Le bouton **Aperçu** le replie si tu préfères un tableau d'état.

**Pour revenir en arrière**, appuie sur **Revenir à l'origine** : le tableau de bord BYD reprend la main. Si jamais il ne revient pas, coupe puis remets le contact.

## Le rail de gauche

| Section | À quoi elle sert |
| --- | --- |
| **Combiné** | L'aperçu en direct, le bouton d'affichage, le choix de l'écran, du mode et du thème. |
| **Contrôle** | Le relevé complet des équipements détectés, avec un bouton pour tout copier. |
| **Journal** | Chaque commande envoyée et chaque réponse reçue. |
| **Réglages** | Langue, apparence, démarrage automatique, accès musique, mises à jour, météo. |

![Combiné](img/tablette-combine.png)

![Réglages](img/tablette-reglages.png)

## Musique

Pour afficher le morceau en cours, VEKTRA a besoin de l'**accès aux notifications** : c'est la règle d'Android pour lire les sessions audio. Appuie sur la ligne **Accès aux notifications** et l'application se l'accorde elle-même par l'ADB, sans rien effacer de la liste existante. Une fois accordé, le titre, l'artiste, la pochette et la progression s'affichent, **quelle que soit l'application qui joue** — radio, Bluetooth, ou une app installée.

## Démarrage et arrêt automatiques

Quand ce réglage est actif, VEKTRA prend le combiné dès que la voiture est allumée et le rend dès qu'elle est coupée. L'état du véhicule est lu **directement dans la voiture**, une fois par seconde : 0 éteint, 1 accessoires, 2 contact mis. Une coupure doit être confirmée deux fois d'affilée avant que l'écran soit rendu — un seul hoquet de la voiture ne doit pas faire disparaître l'affichage en pleine route.

## Apparence

Sombre, claire, ou automatique — l'apparence suit alors celle de la tablette. Le réglage ne concerne que le combiné : l'écran de la tablette reste sombre en toutes circonstances, c'est un poste de pilotage.

## Mise à jour

VEKTRA vérifie toute seule à chaque ouverture. Quand une version est disponible, une fenêtre affiche les nouveautés et propose **Plus tard** ou **Télécharger et installer**. Si tu acceptes, l'application se télécharge, s'installe par-dessus et se rouvre seule. Toutes les versions portent la **même signature** : une mise à jour remplace toujours la précédente sans qu'Android la refuse, et sans perdre les réglages.

## En cas de souci

- **Le combiné reste figé.** Appuie sur *Revenir à l'origine*, puis réessaie. Si rien ne change, coupe et remets le contact.
- **Aucune donnée, que des tirets.** Le SDK de la voiture n'a pas répondu. La section Contrôle dit lesquels des appareils sont joignables.
- **La musique ne s'affiche pas.** L'accès aux notifications n'est pas accordé : voir plus haut. Vérifie aussi que quelque chose joue réellement.
- **La mise à jour dit « Indisponible ».** La tablette n'a pas joint la source. Vérifie sa connexion internet, puis réessaie : la raison exacte s'affiche.
- **Autre chose.** Ouvre *Contrôle*, appuie sur *Copier tout le scan*, puis envoie le texte. Il contient tout ce qu'il faut pour comprendre.

## Nouveautés de la 2.0.2

- Assistant vocal vBot Vektra — Mode Embarqué Natif BYD & Validation Groq :
- Moteur Audio Embarqué Autonome (CarAudioEngine) : l'écoute de « Vektra » et des commandes vocales fonctionne désormais directement sur la tablette BYD sans nécessiter les services Google (GMS) ni aucune application externe. Capture directe du flux microphone via AudioRecord 16 kHz Mono avec seuil VAD adaptatif au bruit de l'habitacle et pré-roll de 300 ms.
- Transcription Instantanée Groq Whisper : transcription vocale ultra-rapide (~180 ms) sur puces LPU pour convertir fidèlement les instructions vocales en texte.
- Correctif et Nettoyage de la Clé API Groq : assainissement automatique des clés collées (retrait des guillemets accidentels, espaces et préfixes "Bearer "), validation réseau directe et statut permanent « ✓ Active & Vérifiée ».
- Permissions Système Renforcées (AppOps) : octroi automatique par ADB de RECORD_AUDIO et OP_RECORD_AUDIO garantissant la transmission matérielle du microphone sous DiLink / Android 10.

---

Projet personnel, sans aucun lien avec BYD. Installation et usage à tes risques. Les informations affichées viennent du système de la voiture et peuvent être inexactes : ne t'y fie jamais pour conduire.
