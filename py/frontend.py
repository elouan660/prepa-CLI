from PySide6.QtWidgets import QMainWindow, QPushButton, QScrollArea, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class OurWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        button = QPushButton("Hi!")
        self.widget = QWidget()
        self.area = QVBoxLayout() #Widgets Verticaux
        self.widget.setLayout(self.area)
        self.area.addWidget(button)
        self.scroller = QScrollArea()
        button.clicked.connect(self.onClick)
    def onClick(self):
        print("Bouton Cliqué")
        self.area.addWidget(QLabel("Test"))
        self.refresh()
    def addentries(self, tab):
        for i in tab:
            self.area.addWidget(QLabel(i))
    def refresh(self):
        self.scroller.setWidget(self.widget)
        self.setCentralWidget(self.scroller)