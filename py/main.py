import create_db
import sys
from PySide6.QtWidgets import QApplication
from frontend import *

app = QApplication(sys.argv) #Créer une aplication qt

window = OurWindow() #Créer une fenêtre (interne à l'application)
window.show() #Afficher la fenêtre 
window.addentries(["tah", "<strong>toh</strong>", "test", "test"])
window.refresh()

app.exec() #Démarrer l'event loop