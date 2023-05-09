import csv #importe la bibliothèque csv

file_csv = open("prepa-scientifiques.csv","r",encoding="utf-8") #Ouvre le fichier csv avec un encodage utf-8
prepa_csv = csv.reader(file_csv,delimiter=";") #Défini le séparateur du csv
prepa_list = [] #Liste qui contiendra toute les données du csv
for ligne in prepa_csv: #ajoute chaque ligne du csv la la liste
    prepa_list.append(ligne)
file_csv.close()
prepa_list.pop(0) #Car le premier élément du tableau n'est pas un lycée mais une description

print("Bienvenue, vsous pouvez ici rechercher une prépa scientifique, vous voulez rechercher une prépa selon Département Filière Nom, laissez le champ vide si vous ne savez pas")

search_lycée = input("Nom du lycée: ")
search_département = input("Numéro du département: ")
search_filière = input("Nom de la filière (ex: MPSI): ")

liste_résultats = [] # Future liste contenant uniquement les formations concernant la requête de l'utilisateur
count = 0
for lycée in prepa_list: #Vérifie ligne par ligne si la formation correspond aux critères demandés par l'utilisateur
    if search_lycée in prepa_list[count][3] and search_département in prepa_list[count][4] and search_filière in prepa_list[count][9] :
        prepa = prepa_list[count][0:17]
        liste_résultats.append(prepa)
    count += 1
print(liste_résultats)

#Créer le fichier résultat.csv contenant les formations répondant à la requête de l'utilisateur
résultats_csv = open("résultats.csv", "w", encoding="utf-8")
for i in liste_résultats:
    for j in i:
        résultats_csv.write(f"{j};")
    résultats_csv.write("\n")
résultats_csv.close()

#Ouvre ou créé le fichier 'main.html', qui contient le rendu graphique final
file_html = open("main.html", "w", encoding="utf-8")
file_html.write(f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href='css/style.css'>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css" integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js" integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=" crossorigin=""></script>
        <title>prepas-scientifiques</title>
    </head>
    <body>
        <div class="container">
            <div class="grid">
            
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
        <h2>{liste_résultats[count][3]} - {liste_résultats[count][9]}</h2>
        
    </section>
    """)
    count += 1

#Ajoute le footer à main.html
file_html.write("""
            </div>
            </div>
            Copyright © Elouan Deschamps<br>
            Le code source de ce site est publié sous licence 
            <a href="https://www.gnu.org/licenses/agpl-3.0.fr.html">
              GNU Affero General Public Licence version 3.0 <br>
              <img src="https://www.gnu.org/graphics/agplv3-88x31.png" alt="agplv3"> <br>
            </a>
            il est diponible sur <a href="https://github.com/elouan660/prepas-scientifiques">Github</a>
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
count = 0
for i in liste_résultats:
    file_js.write(f"""
    L.marker([{liste_résultats[count][16]}]).addTo(map)
    .bindPopup("{liste_résultats[count][12]}")
    .openPopup();
    """)
    count += 1

file_js.close()



