room_data = {
    # --- CITY WALLS NORTH ---
    "From Squire to Knight": {
        "exits": [
            ("Rue Lejour", None),  # To Town Centre East
            ("Traces of Invasion Past", "Iron Key"),
            ("Be for Battle Prepared", None),
        ]
    },
    "Traces of Invasion Past": {
        "exits": [
            ("From Squire to Knight", "Iron Key"),
            ("A Knight Sells his Sword", None),  # To Undercity East
        ]
    },
    "Be for Battle Prepared": {"exits": [("From Squire to Knight", None), ("Destruction and Rebirth", None)]},
    "Destruction and Rebirth": {"exits": [("Be for Battle Prepared", None), ("From Boy to Hero", None)]},
    "From Boy to Hero": {
        "exits": [
            ("Kesch Bridge", None),  # To Town Centre East
            ("Destruction and Rebirth", None),
            ("A Welcome Invasion", "Clematis Sigil"),
        ]
    },
    "A Welcome Invasion": {
        "exits": [
            ("From Boy to Hero", "Clematis Sigil"),
            ("The Greengrocer's Stair", None),  # To Undercity East (North)
        ]
    },
}
