from PySide6.QtWidgets import QMainWindow, QPushButton, QScrollArea

class OurWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        button = QPushButton("Hi!")
        scroller = QScrollArea()
        self.setCentralWidget(scroller)
        button.clicked.connect(self.onClick)
    def onClick(self):
        print("Bouton Cliqué")