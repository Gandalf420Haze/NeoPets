from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
import json

def lade_monster_db():
    with open("monster.json", "r") as f:
        return json.load(f)

class StarterSelectionWindow(QWidget):
    def __init__(self, player_data, speichern_callback):
        super().__init__()

        self.setWindowTitle("Wähle deinen Starter")
        self.setGeometry(100, 100, 400, 200)

        self.player_data = player_data
        self.speichern_callback = speichern_callback
        self.monster_db = lade_monster_db()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Wähle deinen Starter:"))

        for monster in self.monster_db:
            btn = QPushButton(f"{monster['name']} ({monster['type']})")
            btn.clicked.connect(lambda _, m=monster: self.starter_waehlen(m))
            layout.addWidget(btn)

        self.setLayout(layout)

    def starter_waehlen(self, monster):
        self.player_data["starter"] = monster["name"]
        self.speichern_callback(self.player_data)
        self.close()

        # Starte den Kampf automatisch nach Auswahl
        from battle_system import BattleWindow
        self.kampf_window = BattleWindow(self.player_data)
        self.kampf_window.show()
