room_data = {
    "Into Holy Battle": {
        "exits": [
            ("Plateia Lumitar", None),  # To Town Centre East
            ("Struggle for the Soul", None),
            ("The Convent Room", "Truth and Lies"),  # Lever/Event lock
        ]
    },
    "The Poisoned Chapel": {"exits": [("Sin and Punishment", None), ("A Light in the Dark", "Laurel Sigil")]},
    "Sin and Punishment": {
        "exits": [
            ("The Poisoned Chapel", "Flayed Confessional"),  # Cloudstone lock
            ("An Offering of Souls", None),
        ]
    },
    "A Light in the Dark": {"exits": [("The Poisoned Chapel", None)]},
    "The Heretics' Story (Upper)": {
        "exits": [
            ("The Heretics' Story (Lower)", None),  # Drop down
            ("Despair of the Fallen", None),
            ("Where the Soul Rots", "Light and Dark Wage War"),  # Lever lock
        ]
    },
    "The Heretics' Story (Lower)": {"exits": [("The Wine-Lecher's Fall", None), ("Hopes of the Idealist", "Calla Sigil")]},
    "Despair of the Fallen": {"exits": [("The Heretics' Story (Upper)", "Maelstrom of Malice"), ("What Ails You, Kills You", None)]},
    "Hopes of the Idealist": {"exits": [("The Heretics' Story (Lower)", None)]},
    "Where the Soul Rots": {"exits": [("The Heretics' Story (Upper)", None), ("The Atrium", None)]},
}
