progress_window = None
import sys
from PyQt5.QtWidgets import QApplication
from battle_system import BattleWindow
from starter_screen import StarterAuswahl
from progress_screen import ProgressScreen
from utils import (
    lade_player_data,
    speichere_player_data,
    lade_monster_db,
    lade_bot_data
)

def starte_kampf(player_data, monster_db):
    print("Starte Kampf...")
    enemy_data = lade_bot_data(monster_db)

    kampf_fenster = BattleWindow(player_data, enemy_data, monster_db)
    kampf_fenster.kampf_beendet.connect(lambda: zeige_progress_screen(player_data, monster_db))
    kampf_fenster.show()

def zeige_progress_screen(player_data, monster_db):
    global progress_window
    print("Zeige Fortschrittsfenster...")
    progress_window = ProgressScreen(player_data, monster_db, on_back=lambda: starte_kampf(player_data, monster_db))
    progress_window.show()


def starte_app():
    print("Starte App...")
    app = QApplication(sys.argv)
    player_data = lade_player_data()
    monster_db = lade_monster_db()

    if "monster" not in player_data:
        auswahl_screen = StarterAuswahl()

        def nach_auswahl(monster_name):
            player_data["monster"] = monster_name
            player_data["deck"] = ["atk_boost", "def_boost", "spd_boost"]
            player_data["name"] = "Player"
            speichere_player_data(player_data)
            zeige_progress_screen(player_data, monster_db)

        auswahl_screen.starter_ausgewaehlt.connect(nach_auswahl)
        auswahl_screen.show()
    else:
        print("Starter bereits gewählt, zeige ProgressScreen...")
        zeige_progress_screen(player_data, monster_db)

    sys.exit(app.exec_())

if __name__ == '__main__':
    starte_app()
