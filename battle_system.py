from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtCore import pyqtSignal
import random
from utils import finde_monster_daten, lade_monster_db, lade_karten_db, lade_xp_daten, speichere_xp_daten
from xp_manager import gib_xp

class BattleWindow(QWidget):
    kampf_beendet = pyqtSignal()

    def __init__(self, player_data, enemy_data, monster_db):
        super().__init__()
        self.setWindowTitle("Kampf")
        self.player_data = player_data
        self.enemy_data = enemy_data
        self.monster_db = monster_db
        self.karten_db = lade_karten_db()

        self.player_monster = finde_monster_daten(player_data["monster"], monster_db)
        self.enemy_monster = finde_monster_daten(enemy_data["monster"], monster_db)

        self.player_hp = self.player_monster["hp"]
        self.enemy_hp = self.enemy_monster["hp"]

        self.feedback_label = QLabel("")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.player_label = QLabel(f"{self.player_monster['name']} (HP: {self.player_hp})")
        self.enemy_label = QLabel(f"{self.enemy_monster['name']} (HP: {self.enemy_hp})")
        layout.addWidget(self.player_label)
        layout.addWidget(self.enemy_label)
        layout.addWidget(self.feedback_label)

        self.karten_buttons = QHBoxLayout()
        self.card_buttons = []

        for card_id in self.player_data["deck"]:
            btn = QPushButton(self.karten_db[card_id]["name"])
            btn.clicked.connect(lambda checked, c=card_id, b=btn: self.spiele_karte(c, b))
            self.karten_buttons.addWidget(btn)
            self.card_buttons.append(btn)

        layout.addLayout(self.karten_buttons)

        self.angriffs_button = QPushButton("Kämpfen")
        self.angriffs_button.clicked.connect(self.normaler_angriff)
        layout.addWidget(self.angriffs_button)

        self.update_ui()

    def update_ui(self):
        self.player_label.setText(f"{self.player_monster['name']} (HP: {self.player_hp})")
        self.enemy_label.setText(f"{self.enemy_monster['name']} (HP: {self.enemy_hp})")

    def spiele_karte(self, card_id, button):
        effect = self.karten_db[card_id]["effect"]
        value = self.karten_db[card_id]["value"]

        if effect == "atk":
            self.player_monster["atk"] += value
            self.feedback_label.setText(f"ATK +{value}")
        elif effect == "def":
            self.player_monster["def"] += value
            self.feedback_label.setText(f"DEF +{value}")
        elif effect == "spd":
            self.player_monster["spd"] += value
            self.feedback_label.setText(f"SPD +{value}")

        button.setDisabled(True)

    def normaler_angriff(self):
        schaden = max(0, self.player_monster["atk"] - self.enemy_monster["def"])
        self.enemy_hp -= schaden
        self.feedback_label.setText(f"Du greifst an! Schaden: {schaden}")
        self.update_ui()

        if self.enemy_hp <= 0:
            self.beende_kampf(sieger="player")
            return

        self.enemy_zug()

    def enemy_zug(self):
        schaden = max(0, self.enemy_monster["atk"] - self.player_monster["def"])
        self.player_hp -= schaden
        self.feedback_label.setText(f"Der Gegner greift an! Schaden: {schaden}")
        self.update_ui()

        if self.player_hp <= 0:
            self.beende_kampf(sieger="enemy")

    def beende_kampf(self, sieger):
        if sieger == "player":
            xp_daten = lade_xp_daten()
            gib_xp(self.player_data["name"], self.player_monster["name"], 10, xp_daten)
            speichere_xp_daten(xp_daten)
            QMessageBox.information(self, "Sieg!", "Du hast gewonnen und 10 XP erhalten.")
        else:
            QMessageBox.information(self, "Niederlage", "Du hast verloren!")

        self.kampf_beendet.emit()
        self.close()
