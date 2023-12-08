import csv #Manipuler des fichier csv
import requests as req #Récupérer des fichiers en ligne
import os as os #Interagir avec le système hôte
import mysql.connector as sqlco #Utiliser mysql/mariadb
import tkinter as tk #Créer une interface graphique

#Créer des dossiers
if os.path.isdir("prepa-CLI/sql") == False:
    os.mkdir("prepa-CLI/sql")
if os.path.isdir("prepa-CLI/csv") == False:
    os.mkdir("prepa-CLI/csv")

def create_csv(chemin, array, delimiteur, lien):
    if os.path.isfile(chemin) == False:
        get = req.get(lien, allow_redirects=True)
        open(chemin, "wb").write(get.content)
    filecsv = open(chemin, "r", encoding="utf-8")
    db_csv = csv.reader(filecsv,delimiter=delimiteur)
    for ligne in db_csv:
        array.append(ligne)

prepa_array = []
create_csv('prepa-CLI/csv/prepa-scientifiques.csv',prepa_array,";",'https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup/exports/csv?lang=fr&refine=fili%3A%22CPGE%22&refine=form_lib_voe_acc%3A%22Classe%20pr%C3%A9paratoire%20scientifique%22&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B' )
regions_array = []
create_csv('prepa-CLI/csv/regions.csv', regions_array,",","https://www.data.gouv.fr/fr/datasets/r/34fc7b52-ef11-4ab0-bc16-e1aae5c942e7" )
departements_array = []
create_csv('prepa-CLI/csv/departements.csv', departements_array, ",",'https://www.data.gouv.fr/fr/datasets/r/70cef74f-70b1-495a-8500-c089229c0254' )


try: #Se connecter au serveur sql
    prepa_db = sqlco.connect(
        host="localhost",
        user="elouand",
        password="elouan",
        port=3306, #port par défaut mysql
    )
    print("Connection au serveur mysql réussie")
except sqlco.Error as error: #Si un problème empêche la connection au serveur sql
    print(f"ERREUR: {error}")

dbcursor = prepa_db.cursor() #Curseur permettant l'interaction avec le serveur
dbcursor.execute("create database if not exists prepa_db") #créer la base donnée prepa_db
dbcursor.execute("use prepa_db") #La sélectionner, on n'utilisera qu'exclusivement cette db

#Créer les tables (vides) de la base de donnée
def create_tables(ucursor): #uscursor pour "used cursor"
    #créer la table régions listant les régions de france
    ucursor.execute("""
    create table if not exists regions (
        id_region int,
        nom_region varchar(50)
    );""")
    #créer la table départements listant les départements de france en leur assignant une région
    ucursor.execute("""
    create table if not exists departements (
        id_departement int,
        nom_departement varchar(50),
        id_region varchar(50)
    );""")
    #Table des villes
    ucursor.execute("""create table if not exists villes (
        id_ville int,
        nom_ville varchar(50),
        id_departement int
    );""")
    #Tables des status des lycées (privé ou public)
    ucursor.execute("""create table if not exists status (
        id_statut int,
        nom_statut varchar(50)
    );""")
    #Table des lycées
    ucursor.execute("""create table if not exists lycees (
        uai_lycee varchar(9),
        nom_lycee varchar(50),
        id_ville int,
        id_statut int,
        coord_lycee varchar(50)
    );""")
    #Table des fillières (MPSI, MP2I, etc)
    ucursor.execute("""create table if not exists fillieres (
        id_filliere int primary key not null auto_increment,
        nom_filliere varchar(50)
    );""")
    #Table des formations
    ucursor.execute("""create table if not exists formations (
        uai_lycee varchar(9),
        id_filliere int,
        pc_generale float,
        pc_techno float,
        pc_pro float,
        taux_acces float,
        lien_parcoursup varchar(100)
    );""")
create_tables(dbcursor)
for region in regions_array[1:]: #Pour ne pas inclure la première ligne
    requête = f"""
    insert into regions (id_region, nom_region) values ({region[0]}, "{region[1]}") select * from (select {region[0]} as id_region) as temp where not exists(select id_region from regions where id_region = {region[0]});
    """

    dbcursor.execute(requête)
for département in departements_array[1:]:
    corrected_id = département[0] 
    try:
        int(corrected_id) #Si l'id peut est un nombre
    except ValueError: #cas particulier des départements corses
        if département[0][1] == 'A':
            corrected_id = '9001' #Corse du sud
        else:
            corrected_id = '9002' #haute Corse
    dbcursor.execute(f'insert into departements (id_departement, nom_departement, id_region) values ({corrected_id}, "{département[1]}", {département[2]}) ')
for ligne in prepa_array[1:]:
    dbcursor.execute("insert into ")


prepa_db.commit() #Pour valider l'insertion des valeurs
prepa_db.close()