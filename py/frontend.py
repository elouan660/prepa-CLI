from PySide6.QtWidgets import QMainWindow, QPushButton, QScrollArea, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class OurWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test") #Titre de la fenêtre
        button = QPushButton("Hi!")
        self.widget = QWidget() #Widget qui sera le contenu de la scrollarea
        self.area = QVBoxLayout() #Widgets Verticaux
        self.widget.setLayout(self.area) #Mettre self.area dans widget
        self.area.addWidget(button) #Mettre le bouton dans self.area
        self.scroller = QScrollArea() #Créer une zone de scroll
        self.scroller.setWidgetResizable(True) #La rendre redimmensionable (sinon un bug se produit lorsqu'on ajoute un widget)
        button.clicked.connect(self.onClick) #Lancer self.onClick lorsque le bouton est cliqué
    def onClick(self):
        print("Bouton Cliqué")
        self.area.addWidget(QLabel("Test"))
        #self.refresh()
    def addentries(self, tab):
        for i in tab:
            self.area.addWidget(QLabel(i))
    def refresh(self):
        self.scroller.setWidget(self.widget)
        self.setCentralWidget(self.scroller)