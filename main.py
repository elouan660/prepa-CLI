import csv #importe la bibliothèque csv
import requests as req
import os as os

#Crétation de dossiers qui contiendrons des fichier de formats éponymes
if os.path.isdir("css") == False:
    os.mkdir("css")
if os.path.isdir("csv") == False:
    os.mkdir("csv")
if os.path.isdir("js") == False:
    os.mkdir("js")

#Télécharger le fichier csv exploité
if os.path.isfile('csv/prepa-scientifiques.csv') == False:
    fichier = req.get('https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup/exports/csv?lang=fr&refine=fili%3A%22CPGE%22&refine=form_lib_voe_acc%3A%22Classe%20pr%C3%A9paratoire%20scientifique%22&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B', allow_redirects=True)
    open('csv/prepa-scientifiques.csv', "wb").write(fichier.content)

file_csv = open("csv/prepa-scientifiques.csv","r",encoding="utf-8") #Ouvre le fichier csv avec un encodage utf-8
prepa_csv = csv.reader(file_csv,delimiter=";") #Défini le séparateur du csv
prepa_list = [] #Liste qui contiendra toute les données du csv
for ligne in prepa_csv: #ajoute chaque ligne du csv la la liste
    prepa_list.append(ligne)
file_csv.close()
details = prepa_list[0] #stocke la description (header) des données du csv
prepa_list.pop(0) #Car le premier élément du tableau n'est pas un lycée mais une description

print("Bienvenue, vous pouvez ici rechercher une prépa scientifique selon les critères de votre choix, si vous ne répondez pas à une question les résultats de recherche ne la prendrons pas en compte. Une fois que vous avez répondu à toutes les questions, ouvrez le fichier main.html pour accéder aux résultats de recherche")

#Critères utilisateur
search_lycée = input("Nom du lycée: ")
search_département = input("Numéro du département: ")
search_filière = input("Nom de la filière (ex: MPSI): ")
search_status = input("Vous souhaitez des formations se déroulants dans des lycées: Public ou Privé: ")
search_bacg = input("Souhaitez vous voir uniquement des formations qui acceptent les bacheliers généraux?: ")
if search_bacg.upper() == "OUI":
    search_bacpro = 0.0
    search_bactechno = 0.0
    search_bacg = 1.0
else:
    search_bacg = 0.0
    search_bactechno = input("Souhaitez-vous voir uniquement des formations qui acceptent les bacheliers technologiques?: ")  
    if search_bactechno.upper() == "OUI":
        search_bacpro = 0.0
        search_bactechno = 1.0
    else:
        search_bactechno = 0.0
        search_bacpro = input("Souhaitez-vous voir uniquement des formations qui acceptent les bacheliers professionels?: ")
        if search_bacpro.upper() == "OUI":
            search_bacpro = 1.0
        else:
            search_bacpro = 0.0


#Traiter les reponses utilisateur
liste_résultats = [] # Future liste contenant uniquement les formations concernant la requête de l'utilisateur
count = 0
for lycée in prepa_list: #Vérifie ligne par ligne si la formation correspond aux critères demandés par l'utilisateur
    #Ajout de .upper() afin de rendre le champ insensible à la casse
    if search_lycée.upper() in prepa_list[count][3].upper() and search_département in prepa_list[count][4] and search_filière.upper() in prepa_list[count][9].upper() and search_status.upper() in prepa_list[count][1].upper() and prepa_list[count][1].upper() and float(prepa_list[count][88]) >= search_bacg and float(prepa_list[count][90]) >= search_bactechno and float(prepa_list[count][92]) >= search_bacpro:
        prepa = prepa_list[count][0:113] 
        liste_résultats.append(prepa)
    count += 1

#Créer le fichier résultat.csv contenant les formations répondant à la requête de l'utilisateur
résultats_csv = open("csv/rendu.csv", "w", encoding="utf-8")
for i in details:
    résultats_csv.write(f"{i};")
résultats_csv.write("\n")
for i in liste_résultats:
    for j in i:
        résultats_csv.write(f"{j};")
    résultats_csv.write("\n")
résultats_csv.close()

# Génere le fichier css, il n'était pas indispensable de le générer mais ainsi le fichier main.py se suffit à lui même
file_css = open("css/style.css", "w", encoding="utf-8")
file_css.write("""body{
    background-color: #20252b;
    text-align: center;
    font-family: sans-serif;
    color: #9ea5b2;
}
ul{
    list-style-type: none;
    margin-left: auto;
    margin-right: auto;
    text-align: right;
}
button{
    margin-right: 40px;
}
li{
    margin-bottom: 10px;
}

/*Cette classe se nomme grid car à l'origine le contenu davit être stocké dans une grille.
.grid{
    /*display: grid;*/
    width: 90%;
    /*grid-template-columns: 100%;*/
    /*align-items: start;*/
    /*justify-content: space-between;*/
    margin: 10px;
    margin-right: 5%;
    margin-left: 5%;
    padding-right: 0px;
    padding: 5px;
    padding-bottom: 15px;
    background-color: #272b34;
    border-radius: 15px;
}
.form{
    margin-right: 40%;
}
input, button{
    border-radius: 5px;
}
.scroller {
    height: 800px;
    width: 600px;
    margin: auto;
    overflow-y: scroll;
    overflow-x: hidden;
    scroll-snap-type: y none ;
    border: solid;
    border-radius: 15px;
    background-color: #20252b;
}

.scroller section {
    scroll-snap-align: start;
    border-bottom: solid;
}
#map{
    height: 450px; 
    width: 600px;
    margin-left: auto;
    margin-right: auto;
    border-radius: 15px;
    border: solid;
}
/*
@media only screen and (max-device-width: 480px) {
    body{
        background-color: aqua;
    }
    #footer{
        font-size: small;
    }
  }
*/
""")
file_css.close()

#Ouvre ou créé le fichier 'main.html', qui contient le rendu graphique final
file_html = open("main.html", "w", encoding="utf-8")
file_html.write("""<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href='css/style.css'>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css" integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js" integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=" crossorigin=""></script>        <title>prepas-scientifiques</title>
    </head>
    <body>
        <div class="container">
            <div class="grid">
                <div><h1> Résultats de recherche prépas-scientifiques </h1>
                <div>
                    <h2>Carte</h2>
                    <div id = "map"></div>
                    <script src='js/carte.js'></script> <!--Doit être placé après le div d'id map -->
                </div>
                <div>
                    <h2>Liste</h2>
                    <article class="scroller">
""")
file_html.close()
file_html = open("main.html", "a", encoding="utf-8") # Réouvre main.html en mode 'append' car nous allons lui ajouter des informations spécifiques

#Ajoute au fichier main.html toutes les formations répondants aux critères utilisateurs
count = 0
for i in liste_résultats:
    file_html.write(f"""
                    <section>
                        <h3>{liste_résultats[count][3]} - {liste_résultats[count][9]}</h3>
                        Ville: {liste_résultats[count][8]} - Région: {liste_résultats[count][6]} - Département: {liste_résultats[count][5]} <br>
                        Status: {liste_résultats[count][1]} - %BacGénéral {liste_résultats[count][88]} - %BacTech {liste_résultats[count][90]} - %BacPro {liste_résultats[count][92]}
                        - Taux d'accès: {liste_résultats[count][112]}% <br>
                        Fiche parcoursup: <a href="{liste_résultats[count][111]}">lien</a>
                    </section>
""")
    count += 1
if len(liste_résultats) == 0:
    file_html.write("Aucun Résultat")

#Ajoute le footer à main.html
file_html.write("""
                </div>
        </div>
        <div id="footer">
        Copyright © Elouan Deschamps<br>
        Le code source de ce site est publié sous licence 
        <a href="https://www.gnu.org/licenses/agpl-3.0.fr.html">
        GNU Affero General Public Licence version 3.0 <br>
        <img src="https://www.gnu.org/graphics/agplv3-88x31.png" alt="agplv3"> <br>
        </a>
        il est diponible sur <a href="https://github.com/elouan660/prepa-CLI/">Github</a>
        </div>
    </body>
</html>
""")
file_html.close()

#Ouvre ou créé le fichier carte.js qui contient les informations sur la carte leaflet
file_js = open("js/carte.js", "w")
file_js.write("""var map = L.map('map').setView([47.218371, -1.553621], 4);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
""")
file_js.close()
file_js = open("js/carte.js", "a") #Réouvre carte.js en mode append car nous devons lui ajouter des informations spécifiques

map_list = [] #Liste destinée à accueillir les étiquettes des popups de la carte

#Rempli la liste map_list avec uniquement l'intitulé le la formation et ses coordonnées gps
count = 0
for i in liste_résultats:
    multiple = False #Permet de savoir si il un lycée propose plusieurs CPGE
    countj = 0
    for j in map_list:
        #En prévision du cas un lycée propose plusieurs formations
        if liste_résultats[count][16] == map_list[countj][1]:
            map_list[countj][0] += " - " + liste_résultats[count][14]
            multiple = True
        countj += 1
    if multiple == False:
        map_list.append([liste_résultats[count][12], liste_résultats[count][16]])
    count += 1


count = 0
for i in map_list:
    file_js.write(f"""
    L.marker([{map_list[count][1]}]).addTo(map)
    .bindPopup("{map_list[count][0]}")
    .openPopup();
    """)
    count +=1

file_js.close()

print(f"\nPage de résultats générée disponible à {os.getcwd()}/main.html")
print(f"Donnée complètes concernant les résultats disponible à {os.getcwd()}/csv/rendu.csv")