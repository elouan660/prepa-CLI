from PySide6.QtWidgets import QMainWindow, QPushButton, QScrollArea, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QRect, QLine
from PySide6.QtGui import QIcon

class OurWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("prepa_db browser") #Titre de la fenêtre
        icon = QIcon()
        icon.addFile("prepa-CLI/img/Icon.svg")
        self.setWindowIcon(icon)
        self.widget = QWidget() #Widget qui sera le contenu de la scrollarea
        self.area = QVBoxLayout() #Widgets Verticaux
        self.widget.setLayout(self.area) #Mettre self.area dans widget
        self.scroller = QScrollArea() #Créer une zone de scroll
        self.scroller.setWidgetResizable(True) #La rendre redimmensionable (sinon un bug se produit lorsqu'on ajoute un widget)
    def addentries(self, tab):
        for formation in tab:
            self.area.addWidget(QLabel(f"""
            <h3>{formation[0]} - {formation[1]}</h3> <br>
            <strong>Région:</strong> {formation[2]} <strong>Département:</strong> {formation[3]} <strong>Ville:</strong> {formation[4]} <br>
            <strong>Bacheliers Généraux:</strong> {formation[5]}% <strong>Bacheliers Technologiques:</strong> {formation[6]}% <strong>Bacheliers Profesionnels</strong> {formation[7]}% <br>
            <strong>Statut:</strong> {formation[8]} <strong>Taux d'accès:</strong> {formation[9]}%
            <br>
            """))
    def refresh(self):
        self.scroller.setWidget(self.widget)
        self.setCentralWidget(self.scroller)