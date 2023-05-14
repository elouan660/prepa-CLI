# prepa-CLI
Projet NSI 1G5 Livet Elouan Deschamps

Ce projet à pour but de générer une page web renseignant l'utilisateur sur les prépas scientifiques correspondants à ses critères.
Une version récente de python (python 3.9+) ainsi qu'une connection internet sont nécéssaires au fonctionnement du programme

## Frameworks utilisés:
* Html
* Css
* Python (version 3.10.6)
* Javacsript:
    * Leaflet (Cartes interactives)

## Documentation utilisateur
Pour utiliser le programme, téléchargez le fichier `main.py` puis rendez-vous dans le répertoire contenant le fichier avec la commande `cd`, il est recommandé de déplacer le fichier dans un répertoire vide car celui-ci va être ammené à créer d'autres fichiers et repertoires. Vous pouvez ensuite le lancer avec la commande `python3 main.py` sur tout les sytèmes d'exploitation à l'exception de windows ou il faudra entrer `python main.py`.

Il vous sera demandé dans le terminal d'entrez vos critères concernant les CPGE qui pourraient vous intéresser (Nom du lycée, filière, localisation, public/privé, accepte tel ou tel type de bachelier) les champs ne sont pas sensibles à la casse.

Le programme vous indiquera ensuite le chemin d'accès de la page web et d'un fichier csv contenent tout les résultats de recherche. Copiez-collez le chemin d'accès de la page web dans votre navigateur (Testé sous des navigateurs Chromium, Firefox et WebKit)

Vous avez ensuite accès la liste des prépas correspondant à vos critère.

## Documentation développeur
Les codes javascript, html et css sont stockés dans le fichier main.py.
Dans le code main.py, on peut appercevoir des `list[count][x]` (list: liste quelconque, x: nombre quelconque), ceux-ci correspondent aux données téléchargée (chemin d'accès: csv/prepa-scientifiques.csv) sur le site de parcoursup voici la table détaillant la signification du `x` 
x | Description
 --- | --- 
1 | Statut de l'établissement (privé ou public)
3 | Nom de l'établissement
4 | Numéro de département
5 | Nom du département
6 | Nom de la Région
7 | Nom de l'académie
8 | Nom de la ville
9 | Nom de la filière
12 | Nom de l'établissement suivi du nom de la filière
14 | Nom de la filière sans préciser CPGE
16 | Coordonnées GPS
17 | Capacité d'accueil de la formation
88 | % de bacheliers généraux
90 | % de bacheliers technologiques
92 | % de bacheliers professionels
111 | Fiche formation parcoursup
112 | Taux d'accès
## Problèmes rencontrés:
Avec la carte:
* [Résolu] Certains lycée proposent plusieurs formations, fatalement les marqueurs ses chevauchent et des informations ne sont plus accessibles

* 

