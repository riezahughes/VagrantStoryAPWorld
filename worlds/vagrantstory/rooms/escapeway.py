room_data = {
    # --- ESCAPEWAY ---
    "Shelter From the Quake": {
        "exits": [
            ("Path of the Children", None),  # To Undercity West
            ("Buried Alive", "Gold Key"),
            ("Movement of Fear", "Silver Key"),
            ("Fear and Loathing", None),
        ]
    },
    "Buried Alive": {"exits": [("Shelter From the Quake", None)]},
    "Movement of Fear": {"exits": [("Shelter From the Quake", None), ("Facing Your Illusions", None)]},
    "Facing Your Illusions": {"exits": [("Movement of Fear", None), ("The Darkness Drinks", None)]},
    "The Darkness Drinks": {
        "exits": [
            ("Facing Your Illusions", None),
            ("Where Flood Waters Ran", None),  # To Undercity West
        ]
    },
    "Fear and Loathing": {"exits": [("Shelter From the Quake", None), ("Blood and The Beast", None)]},
}
