import csv #Manipuler des fichier csv
import mariadb #Manipuler des bases de données
import requests as req #Récupérer des fichiers en ligne
import os as os #Interagir avec le système hôte
import tkinter as tk #Créer une interface graphique

#Créer des dossiers
if os.path.isdir("prepa-CLI/sql") == False:
    os.mkdir("prepa-CLI/sql")
if os.path.isdir("prepa-CLI/csv") == False:
    os.mkdir("prepa-CLI/csv")

prepa_db = mariadb.connect(
    host="localhost",
    user="elouand",
    password="elouan",
    port=3306,
)
mycursor = prepa_db.cursor()
mycursor.execute("SELECT * FROM albums")
myresult = mycursor.fetchall()

for i in myresult:
    print(i)
