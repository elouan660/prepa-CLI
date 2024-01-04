import csv #Manipuler des fichier csv
import requests as req #Récupérer des fichiers en ligne
import os #Interagir avec le système hôte
import sys
import mysql.connector as sqlco #Utiliser mysql/mariadb

class dbmanager:
    def __init__():
        self.projectpath = 'prepa-CLI/'
        self.prepa_array = []
        self.regions_array = []
        self.departements_array = []
        create_csv(f'{self.projectpath}/csv/prepa-scientifiques.csv',self.prepa_array,";",'https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup/exports/csv?lang=fr&refine=fili%3A%22CPGE%22&refine=form_lib_voe_acc%3A%22Classe%20pr%C3%A9paratoire%20scientifique%22&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B' )
        create_csv(f'{self.projectpath}/csv/regions.csv', self.regions_array,",","https://www.data.gouv.fr/fr/datasets/r/34fc7b52-ef11-4ab0-bc16-e1aae5c942e7" )
        create_csv(f'{self.projectpath}/csv/departements.csv', self.departements_array, ",",'https://www.data.gouv.fr/fr/datasets/r/70cef74f-70b1-495a-8500-c089229c0254' )


    def create_csv(chemin, array, delimiteur, lien):
        if os.path.isfile(chemin) == False:
            get = req.get(lien, allow_redirects=True)
            open(chemin, "wb").write(get.content)
        filecsv = open(chemin, "r", encoding="utf-8")
        db_csv = csv.reader(filecsv, delimiter=delimiteur)
        for ligne in db_csv:
            array.append(ligne)