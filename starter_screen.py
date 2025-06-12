from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import pyqtSignal

class StarterAuswahl(QWidget):
    starter_ausgewaehlt = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wähle dein Starter-Monster")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        hinweis = QLabel("Wähle dein Starter-Monster:")
        layout.addWidget(hinweis)

        # Liste der verfügbaren Starter-Monster (muss mit monster_db.json übereinstimmen)
        starter_monster = ["flamio", "aquata", "leafix"]

        for monster_name in starter_monster:
            btn = QPushButton(monster_name.capitalize())
            btn.clicked.connect(lambda _, name=monster_name: self.starter_waehlen(name))
            layout.addWidget(btn)

        self.setLayout(layout)

    def starter_waehlen(self, monster_name):
        self.starter_ausgewaehlt.emit(monster_name)
        self.close()
