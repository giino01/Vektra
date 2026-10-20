<div align="center">

# V E K T R A

**Le combiné de ta BYD, à ta façon.**

Tableau de bord personnalisé pour l'écran derrière le volant des véhicules BYD DiLink 3.

**Version 1.4.3** · publiée le 20 octobre 2026 · 2.7 Mo

[**Télécharger l'APK**](https://giino01.github.io/Vektra/Vektra-1.4.3.apk) · [**Page du projet**](https://giino01.github.io/Vektra/)

</div>

---

## Aperçu

![Le combiné en ambiance bleue](img/combine-normal.png)

De gauche à droite : l'heure et la date, le compteur à aiguille gradué jusqu'à 220 km/h,
la musique en cours quelle que soit l'application qui la joue, trois chiffres choisis selon
le mode, la ligne de flux d'énergie, la météo animée et la pression des quatre pneus en bar.

![Le combiné en ambiance rouge, mode Sport](img/combine-sport.png)

En Sport — détecté automatiquement par la voiture — l'ambiance passe au rouge, une pastille
`SPORT` apparaît, et les trois chiffres du bas deviennent puissance, régime et accélérateur.

> Ces captures sont **dessinées par le code de la version 1.4.3** à chaque
> publication, avec des valeurs de démonstration. Elles ne peuvent pas dater d'une version
> précédente.

## Ce qu'il faut

- Un véhicule **BYD équipé de DiLink 3** (Android 10). Mis au point sur une Seal U DM-i ;
  les autres modèles DiLink 3 n'ont pas été vérifiés.
- L'installation d'applications extérieures autorisée sur la tablette.
- Le **débogage ADB en réseau** actif sur le port 5555. VEKTRA s'y connecte en local, sur
  la tablette elle-même : rien ne sort du véhicule.
- Une connexion internet pour la météo et les mises à jour. Tout le reste marche hors ligne.

Les commandes qui libèrent l'écran du combiné ne sont autorisées qu'à l'utilisateur `shell`
d'Android : une application ordinaire ne peut pas les envoyer. C'est pourquoi VEKTRA passe
par l'ADB local.

## Installation

1. Télécharge [`Vektra-1.4.3.apk`](https://giino01.github.io/Vektra/Vektra-1.4.3.apk) sur la tablette et ouvre-le.
2. Au premier démarrage, choisis la langue, puis **Continuer**.
3. Section **Contrôle** → **Vérifier · ADB et diagnostic**.
4. À la demande **« Autoriser le débogage USB ? »**, coche **Toujours autoriser**, puis
   accepte. Elle n'apparaît qu'une fois.
5. Section **Combiné** → **Afficher sur le combiné**. Une dizaine de secondes plus tard,
   l'affichage apparaît derrière le volant.

Pour revenir en arrière : **Revenir à l'origine**. Si le tableau de bord BYD ne revient pas,
coupe et remets le contact.

![Écran d'accueil et choix de la langue](img/accueil-langue.png)

## Les quatre sections

| Section | À quoi elle sert |
| --- | --- |
| **Combiné** | L'aperçu en direct, le bouton d'affichage, le choix de l'écran et du mode. |
| **Contrôle** | Le relevé complet des équipements détectés, avec un bouton pour tout copier. |
| **Journal** | Chaque commande envoyée et chaque réponse reçue. |
| **Réglages** | Langue, démarrage automatique, accès musique, mises à jour, météo. |

![Section Combiné](img/tablette-combine.png)

![Section Réglages](img/tablette-reglages.png)

## Musique

Pour afficher le morceau en cours, Android exige l'**accès aux notifications**. La ligne
correspondante dans les réglages l'accorde par l'ADB, sans rien effacer de la liste
existante. Une fois accordé, le titre, l'artiste, la pochette et la progression s'affichent
quelle que soit l'application qui joue.

## Démarrage et arrêt automatiques

L'état du véhicule est lu directement dans la voiture, une fois par seconde :
0 éteint, 1 accessoires, 2 contact mis. VEKTRA prend le combiné à l'allumage et le rend à
l'extinction. Une coupure doit être confirmée deux fois d'affilée avant que l'écran soit
rendu : un hoquet isolé ne doit pas faire disparaître l'affichage en pleine route.

## Mises à jour

L'application vérifie toute seule à chaque ouverture, affiche les nouveautés, puis
télécharge, installe et se rouvre si tu acceptes. Toutes les versions portent la même
signature, donc une mise à jour remplace la précédente sans perdre les réglages.
L'adresse consultée se change dans les réglages, sans recompiler.

## En cas de souci

Ouvre **Contrôle**, appuie sur **Copier tout le scan**, et envoie le texte : il contient
l'état de tous les équipements, de l'ADB, de la musique, de l'alimentation et des mises à
jour.

## Nouveautés de la 1.4.3

- L'heure n'est plus affichée : la surcouche BYD la donne déjà juste au-dessus.
- La date passe au-dessus de la carte musique, et la pastille SPORT descend dans le cadran, sous « km/h ».
- Le fond s'éclaircit plus loin vers le centre : la limite avec la surcouche BYD ne se voit plus à mi-chemin.

---

Projet personnel, sans aucun lien avec BYD. Installation et usage à tes risques.
Les informations affichées viennent du système de la voiture et peuvent être inexactes :
ne t'y fie jamais pour conduire.
