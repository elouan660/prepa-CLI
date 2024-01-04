import create_db
import sys
from PySide6.QtWidgets import QApplication
from frontend import OurWindow

app = QApplication() #Créer une aplication qt
create_db.ext_create_tables() #Créer les tables de la base de données
create_db.ext_remp_tables() #Les remplir
window = OurWindow() #Créer une fenêtre (interne à l'application)
window.resize(850,600)
window.show() #Afficher la fenêtre 
#window.refresh()
window.addfillieres(create_db.getfilliere())
window.adddepartements(create_db.getdepartements())
window.addregions(create_db.getregions())
#Une fonction lamba puisqu'il faut une fonction sans paramètres en paramètre
window.submitbutton.clicked.connect(lambda: window.submit(tab=create_db.getentries(departement_ext=window.departement.currentText(), filliere_ext=window.fillieres.currentText(), region_ext=window.regions.currentText())))

app.exec() #Démarrer l'event loop