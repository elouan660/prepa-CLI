import create_db
import sys
from PySide6.QtWidgets import QApplication
from frontend import *

app = QApplication(sys.argv) #Créer une aplication qt
create_db.ext_create_tables() #Créer les tables de la base de données
create_db.ext_remp_tables() #Les remplir
window = OurWindow() #Créer une fenêtre (interne à l'application)
window.resize(800,600)
window.show() #Afficher la fenêtre 
window.refresh()
window.addentries(create_db.getentries())

app.exec() #Démarrer l'event loop