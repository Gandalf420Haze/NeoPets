import json
import random
import os
from xp_manager import gib_xp
# Am Ende von utils.py
__all__ = ["lade_player_data", "speichere_player_data", "lade_monster_db", "lade_karten_db", "lade_bot_data", "finde_monster_daten", "gib_xp"]

def lade_json(pfad):
    if not os.path.exists(pfad):
        return {}
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)

def speichere_json(pfad, daten):
    with open(pfad, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4)

def lade_player_data():
    return lade_json("player_data.json")

def speichere_player_data(data):
    speichere_json("player_data.json", data)

def lade_monster_db():
    return lade_json("monster.json")

def lade_karten_db():
    return lade_json("karten_db.json")

def lade_xp_daten():
    if not os.path.exists("xp.json"):
        return {}
    with open("xp.json", "r", encoding="utf-8") as f:
        return json.load(f)

def speichere_xp_daten(xp_daten):
    with open("xp.json", "w", encoding="utf-8") as f:
        json.dump(xp_daten, f, indent=4)

def lade_bot_data(monster_db):
    monster_namen = list(monster_db.keys())
    zufalls_monster = random.choice(monster_namen)
    return {
        "name": "Bot",
        "monster": zufalls_monster,
        "deck": ["atk_boost", "def_boost", "spd_boost"]
    }

def finde_monster_daten(monster_info, monster_db):
    if isinstance(monster_info, dict):
        monster_name = monster_info.get("name", None)
    else:
        monster_name = monster_info
    return monster_db.get(monster_name, None)
    lade_karten_db = lade_karten_daten  # Alias zur Kompatibilität

