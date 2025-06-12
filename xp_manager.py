import json
import os

XP_DATEI = "xp.json"

def lade_xp_daten():
    if not os.path.exists(XP_DATEI):
        return {}
    with open(XP_DATEI, "r") as f:
        return json.load(f)

def speichere_xp_daten(daten):
    with open(XP_DATEI, "w") as f:
        json.dump(daten, f, indent=4)

def gib_xp(spieler_name, monster_name, menge, daten):
    if spieler_name not in daten:
        daten[spieler_name] = {}
    if monster_name not in daten[spieler_name]:
        daten[spieler_name][monster_name] = 0
    daten[spieler_name][monster_name] += menge
    print(f"XP vergeben: {menge} an {spieler_name}/{monster_name}")

def lade_xp_stand(spieler_name, monster_name, daten):
    return daten.get(spieler_name, {}).get(monster_name, 0)
