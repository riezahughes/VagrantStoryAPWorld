room_data = {
    # --- CITY WALLS SOUTH ---
    "In Wait of the Foe": {
        "exits": [
            ("Villeport Way", None),  # Connection to Town Centre West (Latch side)
            ("Swords for the Land", None),
            ("Where Weary Riders Rest", None),
        ]
    },
    "Swords for the Land": {"exits": [("In Wait of the Foe", None), ("The Weeping Boy", None)]},
    "The Weeping Boy": {
        "exits": [
            ("Swords for the Land", None),
            ("The Wood Gate", None),  # To Snowfly Forest
        ]
    },
    "Where Weary Riders Rest": {"exits": [("In Wait of the Foe", None), ("The Boy's Training Room", None)]},
    "The Boy's Training Room": {
        "exits": [
            ("Where Weary Riders Rest", None),
            ("The Soldier's Bedding", None),  # To The Keep
            # Note: The North exit from Town Center South is a latch,
            # so it is not listed as an exit from here.
        ]
    },
}
