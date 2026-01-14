room_data = {
    # --- CITY WALLS EAST ---
    "Train and Grow Strong": {
        "exits": [
            ("Rue Volnac", None),  # To Town Centre South
            ("The Squire's Gathering", None),
            ("Steady the Boar-Spears", "Rood Inverse"),  # To Snowfly Forest East (NG+)
        ]
    },
    "The Squire's Gathering": {"exits": [("Train and Grow Strong", None), ("The Invaders are Found", None)]},
    "The Invaders are Found": {
        "exits": [
            ("The Squire's Gathering", None),
            ("Rue Volnac", None),  # This is the latch into Town Centre South
            ("The Dream Weavers", None),
        ]
    },
    "The Dream Weavers": {"exits": [("The Invaders are Found", None), ("The Cornered Savage", None)]},
    "The Cornered Savage": {
        "exits": [
            ("The Dream Weavers", None),
            ("Fear of the Fall", None),  # To Undercity West
        ]
    },
}
