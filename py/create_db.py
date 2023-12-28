import csv #Manipuler des fichier csv
import requests as req #Récupérer des fichiers en ligne
import os #Interagir avec le système hôte
import sys
import mysql.connector as sqlco #Utiliser mysql/mariadb
 
def create_csv(chemin, array, delimiteur, lien):
    if os.path.isfile(chemin) == False:
        get = req.get(lien, allow_redirects=True)
        open(chemin, "wb").write(get.content)
    filecsv = open(chemin, "r", encoding="utf-8")
    db_csv = csv.reader(filecsv, delimiter=delimiteur)
    for ligne in db_csv:
        array.append(ligne)

prepa_array = []
create_csv('prepa-CLI/csv/prepa-scientifiques.csv',prepa_array,";",'https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup/exports/csv?lang=fr&refine=fili%3A%22CPGE%22&refine=form_lib_voe_acc%3A%22Classe%20pr%C3%A9paratoire%20scientifique%22&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B' )
regions_array = []
create_csv('prepa-CLI/csv/regions.csv', regions_array,",","https://www.data.gouv.fr/fr/datasets/r/34fc7b52-ef11-4ab0-bc16-e1aae5c942e7" )
departements_array = []
create_csv('prepa-CLI/csv/departements.csv', departements_array, ",",'https://www.data.gouv.fr/fr/datasets/r/70cef74f-70b1-495a-8500-c089229c0254' )

#Créer des dossiers
if os.path.isdir("prepa-CLI/sql") == False:
    os.mkdir("prepa-CLI/sql")
if os.path.isdir("prepa-CLI/csv") == False:
    os.mkdir("prepa-CLI/csv")


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
#Il est néscéssaire de préciser la primary key pour éviter qu'un enregistrement ne puisse apparaitre en double
def create_tables(ucursor): #uscursor pour "used cursor"
    #créer la table régions listant les régions de france
    ucursor.execute("""
    create table if not exists regions (
        id_region int primary key,
        nom_region varchar(50)
    );""")
    #créer la table départements listant les départements de france en leur assignant une région
    ucursor.execute("""
    create table if not exists departements (
        id_departement int primary key,
        nom_departement varchar(50),
        id_region varchar(50)
    );""")
    #Table des villes
    ucursor.execute("""create table if not exists villes (
        id_ville int primary key not null auto_increment,
        nom_ville varchar(50),
        id_departement int
    );""")
    #Tables des status des lycées (privé ou public)
    ucursor.execute("""create table if not exists status (
        id_statut int primary key not null auto_increment,
        nom_statut varchar(50)
    );""")
    #Table des lycées
    ucursor.execute("""create table if not exists lycees (
        uai_lycee varchar(9) primary key,
        nom_lycee varchar(50),
        id_ville int,
        id_statut int,
        coord_lycee varchar(50)
    );""")
    #Table des fillières (MPSI, MP2I, etc)
    ucursor.execute("""create table if not exists fillieres (
        id_filliere int primary key not null auto_increment,
        nom_filliere varchar(100)
    );""")
    #Table des formations
    ucursor.execute("""create table if not exists formations (
        id_formation int primary key not null auto_increment,
        uai_lycee varchar(9),
        id_filliere int,
        pc_generale float,
        pc_techno float,
        pc_pro float,
        taux_acces float,
        lien_parcoursup varchar(150)
    );""")

def ext_create_tables():
    try:
        create_tables(dbcursor)
        print("Tables crées sans erreur")
    except sqlco.Error as error:
        print(f"ERREUR: {error}")

def ext_remp_tables():
    #Créer les enregistrements de la table regions
    for region in regions_array[1:]: #Pour ne pas inclure la première ligne
        requête = f'insert ignore into regions (id_region, nom_region) values ({region[0]}, "{region[1]}")' #insert ignore pour ne rien faire si l'enregistrement existe déjà
        dbcursor.execute(requête)
    #Créer les enregistrements de la table departements
    for département in departements_array[1:]:
        corrected_dep = département[0] 
        try:
            int(corrected_dep) #Si l'id peut est un nombre entier
        except ValueError: #cas particulier des départements corses
            if département[0][1] == 'A':
                corrected_dep = '9001' #Corse du sud
            else:
                corrected_dep = '9002' #haute Corse
        dbcursor.execute(f'insert ignore into departements (id_departement, nom_departement, id_region) values ({corrected_dep}, "{département[1]}", {département[2]}) ')
    #Créer les enregistrements des status, des villes, des lycées, des fillières et enfin des Formations
    for formation in prepa_array[1:]:
        corrected_dep = formation[4] 
        try:
            int(corrected_dep) #Si l'id peut est un nombre entier
        except ValueError: #cas particulier des départements corses
            if formation[4][1] == 'A':
                corrected_dep = '9001' #Corse du sud
            else:
                corrected_dep = '9002' #haute Corse
        dbcursor.execute(f'insert into status (nom_statut) select "{formation[1]}" from dual where not exists (select * from status where nom_statut = "{formation[1]}");')
        dbcursor.execute(f'select id_statut from status where nom_statut = "{formation[1]}"') #Retrouver l'id (automatiquement attribuée) du statut
        current_statut = dbcursor.fetchall()[0][0] #id du statut courant
        dbcursor.execute(f'insert into villes (nom_ville, id_departement) select "{formation[8]}", {corrected_dep} from dual where not exists (select * from villes where nom_ville = "{formation[8]}");')
        dbcursor.execute(f'select id_ville from villes where nom_ville = "{formation[8]}"')
        current_ville = dbcursor.fetchall()[0][0] #id de la ville courante
        dbcursor.execute(f'insert ignore into lycees (uai_lycee, nom_lycee, id_ville, id_statut, coord_lycee) values ("{formation[2]}", "{formation[3]}", {current_ville}, {current_statut}, "{formation[16]}" )')
        dbcursor.execute(f'insert into fillieres (nom_filliere) select "{formation[14]}" from dual where not exists (select * from fillieres where nom_filliere = "{formation[14]}")')
        dbcursor.execute(f'select id_filliere from fillieres where nom_filliere = "{formation[14]}"')
        current_filliere = dbcursor.fetchall()[0][0] #id de la filliere courante
        dbcursor.execute(f'insert into formations (uai_lycee, id_filliere, pc_generale, pc_techno, pc_pro, taux_acces, lien_parcoursup) select "{formation[2]}", {current_filliere}, {formation[88]}, {formation[90]}, {formation[92]}, {formation[112]}, "{formation[111]}" from dual where not exists (select * from formations where uai_lycee = "{formation[2]}" and id_filliere = {current_filliere})')

    prepa_db.commit() #Pour valider l'insertion des valeurs
    print("Tables remplies sans erreur")

def getdepartements():
    dbcursor.execute(f'select id_departement from departements')
    return dbcursor.fetchall()
def getregions():
    dbcursor.execute(f'select nom_region from regions')
    return dbcursor.fetchall()
def getfilliere():
    dbcursor.execute(f'select nom_filliere from fillieres')
    return dbcursor.fetchall()

def getentries(filliere_ext="", region_ext="", departement_ext=""):
    #Requête du démon extrayant l'entièreté des données de la db; correction du problème des prépa PTSI confondues avec des TSI
    dbcursor.execute(f'select nom_lycee, nom_filliere, nom_region, nom_departement, nom_ville, pc_generale, pc_techno, pc_pro, nom_statut, taux_acces, lien_parcoursup from formations inner join lycees on formations.uai_lycee = lycees.uai_lycee inner join fillieres on formations.id_filliere = fillieres.id_filliere inner join status on lycees.id_statut = status.id_statut inner join villes on lycees.id_ville = villes.id_ville inner join departements on villes.id_departement = departements.id_departement inner join regions on departements.id_region = regions.id_region where nom_filliere like "{filliere_ext}%" and nom_region like "%{region_ext}%" and departements.id_departement like "%{departement_ext}%"')
    return dbcursor.fetchall()