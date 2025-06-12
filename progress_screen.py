from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from xp_manager import lade_xp_daten, lade_xp_stand

class ProgressScreen(QWidget):
    def __init__(self, player_data, monster_db, on_back):
        super().__init__()
        self.setWindowTitle("Fortschritt")
        self.player_data = player_data
        self.monster_db = monster_db
        self.on_back = on_back
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        xp_daten = lade_xp_daten()
        player_name = self.player_data.get("name", "Player")
        monster_name = self.player_data.get("monster", "flamio")

        # Player-XP anzeigen
        player_xp = lade_xp_stand(player_name, monster_name, xp_daten)
        layout.addWidget(QLabel(f"Spieler: {player_name}"))
        layout.addWidget(QLabel(f"Monster: {monster_name}"))
        layout.addWidget(QLabel(f"XP: {player_xp}"))

        # Zurück zum Kampf-Button
        btn_back = QPushButton("Zurück zum Kampf")
        btn_back.clicked.connect(self.zurueck_zum_kampf)
        layout.addWidget(btn_back)

        self.setLayout(layout)

    def zurueck_zum_kampf(self):
        self.close()
        self.on_back()
