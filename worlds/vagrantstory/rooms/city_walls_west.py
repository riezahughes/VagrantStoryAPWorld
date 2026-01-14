room_data = {
    # --- CITY WALLS WEST ---
    "Students of Death": {
        "exits": [
            ("Rue Vermillion", "Crimson Key"),  # To Town Centre West
            ("The Gabled Hall", None),
        ]
    },
    "The Gabled Hall": {"exits": [("Students of Death", None), ("Where the Master Fell", None)]},
    "Where the Master Fell": {
        "exits": [
            ("The Gabled Hall", None),
            ("Dreamers' Entrance", None),  # To Abandoned Mines B1
        ]
    },
}
