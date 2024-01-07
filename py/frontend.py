#Copyright 2024 Elouan Deschamps
#Ce fichier est publié sous licence GNU GPLv3
#Fichier contenant la classe gérant la fenêtre principale
from PySide6.QtWidgets import QMainWindow, QPushButton, QScrollArea, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QComboBox
from PySide6.QtCore import Qt, QRect, QLine
from PySide6.QtGui import QIcon, QPixmap

class OurWindow(QMainWindow): #Héritage de QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("prepa_db browser") #Titre de la fenêtre
        icon = QIcon()
        icon.addFile("img/Icon.svg")
        self.setWindowIcon(icon)
        #QSS, Un peu différent du css
        self.setStyleSheet("""
        [cadre="true"]:hover {
            border: 1px solid grey;
        } 
        [right="true"] {
            qproperty-alignment: AlignRight;
        }
        QPushButton {
            background-color: blue;
            color: white;
        }
        """)
        self.widget = QWidget() #Widget qui sera le contenu de la scrollarea
        self.area = QVBoxLayout() #Widgets Verticaux
        self.widget.setLayout(self.area) #Mettre self.area dans widget
        self.scroller = QScrollArea() #Créer une zone de scroll
        self.scroller.setWidgetResizable(True) #La rendre redimmensionable (sinon un bug se produit lorsqu'on ajoute un widget)

        self.bigwidget = QWidget()
        self.bigarea = QVBoxLayout()
        self.bigwidget.setLayout(self.bigarea)
        self.bigbar = QWidget()
        self.bigbarbox = QHBoxLayout()
         #Comboxbox des fillières
        self.fillieres = QComboBox()
         #Combobox des départements
        self.departement = QComboBox()
        #self.departement.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
         #Combobox des regions
        self.regions = QComboBox()
         #Submit button
        self.submitbutton = QPushButton("Rechercher")

        self.fillierelabel = QLabel("Fillière:")
        self.fillierelabel.setProperty("right", True)
        self.bigbarbox.addWidget(self.fillierelabel)
        self.bigbarbox.addWidget(self.fillieres)

        self.regionslabel = QLabel("Région:")
        self.regionslabel.setProperty("right", True)
        self.bigbarbox.addWidget(self.regionslabel)
        self.bigbarbox.addWidget(self.regions)

        self.departementlabel = QLabel("Département:")
        self.departementlabel.setProperty("right", True)
        self.bigbarbox.addWidget(self.departementlabel)
        self.bigbarbox.addWidget(self.departement)

        self.bigbarbox.addWidget(self.submitbutton)
        self.bigbar.setLayout(self.bigbarbox)
        self.bigarea.addWidget(self.bigbar)
        self.numberofresultslabel = QLabel('Cliquez sur "Rechercher" pour lancer une recherche')
        self.bigarea.addWidget(self.numberofresultslabel)
        self.bigarea.addWidget(self.scroller)

        self.scroller.setWidget(self.widget) #Mettre le widget dans la scrollarea
        self.setCentralWidget(self.bigwidget)

    def addentries(self, tab):
        for formation in tab:
            #HTML4 like
            templab = QLabel(f"""
            <div>
                <h3>{formation[0]} - {formation[1]}</h3> <br>
                <strong><u>Région:</strong></u> {formation[2]} <strong><u>Département:</strong></u> {formation[3]} <strong><u>Ville:</strong></u> {formation[4]} <br>
                <strong><u>Bacheliers Généraux:</strong></u> {formation[5]}% <strong><u>Bacheliers Technologiques:</strong></u> {formation[6]}% <strong><u>Bacheliers Profesionnels:</strong></u> {formation[7]}% <br>
                <strong><u>Statut:</strong></u> {formation[8]} <strong><u>Taux d'accès:</strong></u> {formation[9]}%
                <a href="{formation[10]}">Lien Parcoursup</a>
                <br>
            </div>
            """)
            templab.setProperty("cadre", True)
            templab.setOpenExternalLinks(True) #Pour rendre les liens cliquable
            self.area.addWidget(templab)
    def adddepartements(self, tab):
        self.departement.addItems([""])
        for departement in tab:
            self.departement.addItems([str(departement[0])])
    def addregions(self, tab):
        self.regions.addItems([""])
        for region in tab:
            self.regions.addItems([region[0]])
    def addfillieres(self, tab):
        self.fillieres.addItems([""])
        for filliere in tab:
            self.fillieres.addItems([filliere[0]])
    def submit(self, tab):
        print("Submitted")
        while self.area.count() > 0: #Supprimer tous les widgets contenus dans La Vbox de la scrollarea
            item = self.area.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())
        self.addentries(tab)
        self.numberofresultslabel.setText(f'{len(tab)} Résultats')