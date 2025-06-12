# xp_system.py

def get_required_xp(level):
    return 50 + (level - 1) * 25

def add_xp(entity_data, amount):
    leveled_up = False
    entity_data["xp"] += amount
    while entity_data["xp"] >= get_required_xp(entity_data["level"]):
        entity_data["xp"] -= get_required_xp(entity_data["level"])
        entity_data["level"] += 1
        leveled_up = True
    return leveled_up
