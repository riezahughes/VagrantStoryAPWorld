room_data = {
    "Into Holy Battle": {"exits": [("Plateia Lumitar", None), ("Struggle for the Soul", None), ("The Convent Room", "Truth and Lies")]},
    "The Poisoned Chapel": {"exits": [("Sin and Punishment", None), ("A Light in the Dark", "Laurel Sigil")]},
    "Sin and Punishment": {
        "exits": [("The Poisoned Chapel", "Flayed Confessional"), ("An Offering of Souls", None)],
        "save_point": True,
        "container": True,
        "traps": ["Curse Panel", "Eruption"],
    },
    "A Light in the Dark": {"exits": [("The Poisoned Chapel", None)], "miniboss": "Arch Dragon"},
    "Monk's Leap": {"exits": [("The Acolyte's Weakness", None)], "miniboss": "Lich"},
    "Hieratic Recollections": {"exits": [("The Flayed Confessional", None), ("Cracked Pleasures", None)]},
    "The Flayed Confessional": {"exits": [("Hieratic Recollections", None)], "boss": "Djinn"},
    "Cracked Pleasures": {"exits": [("Hieratic Recollections", None), ("The Victor's Laurels", None), ("Free from Base Desires", None)]},
    "Where Darkness Spreads": {"exits": [("An Arrow into Darkness", None)]},
}
