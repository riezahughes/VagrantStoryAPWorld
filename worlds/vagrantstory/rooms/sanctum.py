room_data = {
    # --- SANCTUM ---
    "Prisoners' Niche": {"exits": [("The Withered Spring", None), ("Corridor of the Clerics", None)]},
    "Corridor of the Clerics": {
        "exits": [("Prisoners' Niche", None), ("Priests' Confinement", None), ("Advent Ground (South)", None), ("The Academia Corridor", None)]
    },
    "Priests' Confinement": {"exits": [("Corridor of the Clerics", None), ("Alchemists' Laboratory", None)]},
    "Alchemists' Laboratory": {"exits": [("Priests' Confinement", None), ("The Academia Corridor", None)]},
    "The Academia Corridor": {
        "exits": [
            ("Corridor of the Clerics", None),
            ("Theology Classroom", None),
            ("Shrine of the Martyrs", None),
            # Exit to Alchemists' Lab is locked from the other side (latch)
        ]
    },
    "Advent Ground (South)": {"exits": [("Corridor of the Clerics", None), ("Passage of the Refugees (South)", None)]},
    "Passage of the Refugees (South)": {
        "exits": [
            ("Advent Ground (South)", None),
            ("Passage of the Refugees (North)", "Hall of Sacrilege"),  # Boss Event Lock
        ]
    },
    "Passage of the Refugees (North)": {"exits": [("Passage of the Refugees (South)", None), ("Advent Ground (North)", None)]},
    "Advent Ground (North)": {"exits": [("Passage of the Refugees (North)", None), ("The Cleansing Chantry", None)]},
    "The Cleansing Chantry": {"exits": [("Advent Ground (North)", None), ("Stairway to the Light", None)]},
}
