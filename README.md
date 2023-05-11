# prepa-CLI
Projet NSI 1G5 Livet Elouan Deschamps

Ce projet à pour but de générer un site web renseignant l'utilisateur sur les prépas scientifiques correspondants à ses critères.
Seul le fichier main.py et une connection internet (pas besoin d'un débit gargantuesque) sont néscéssaires pour le bon usage du programme.

## Frameworks utilisés:
* Html
* Css
* Python (Abandon de Django)
* Javacsript:
    * Leaflet (Cartes interactives)
    * Chartjs (Graphiques élégants) 

## Documentation
Dans le code main.py, on peut appercevoir des `list[count][x]` (list: liste quelconque, x: nombre quelconque), voci la table détaillant la signification du `x` 
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
88 | % de bacheliers généraux
90 | % de bacheliers technologiques
92 | % de bacheliers professionels

## Problèmes rencontrés:
Avec la carte:
* [Résolu] Certains lycée proposent plusieurs formations, fatalement les markeurs ses chevauchent et des informations ne sont plus accessibles

