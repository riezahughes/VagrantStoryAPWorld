room_data = {
    "Prisoners' Niche": {"exits": [("The Withered Spring", None), ("Corridor of the Clerics", None)]},
    "Corridor of the Clerics": {
        "exits": [("Prisoners' Niche", None), ("Priests' Confinement", None), ("Advent Ground (South)", None), ("The Academia Corridor", None)]
    },
    "Priests' Confinement": {"exits": [("Corridor of the Clerics", None), ("Alchemists' Laboratory", None)]},
    "Alchemists' Laboratory": {"exits": [("Priests' Confinement", None), ("The Academia Corridor", None)], "container": True},
    "The Academia Corridor": {
        "exits": [("Corridor of the Clerics", None), ("Theology Classroom", None), ("Shrine of the Martyrs", None)],
        "notes": "East exit to Alchemists' Laboratory must be unlocked from the lab side.",
    },
    "Theology Classroom": {"exits": [("The Academia Corridor", None)], "notes": "Dead end cage match."},
    "Shrine of the Martyrs": {"exits": [("The Academia Corridor", None), ("Hallowed Hope", None)]},
    "Hallowed Hope": {"exits": [("Shrine of the Martyrs", None), ("Hall of Sacrilege", None)]},
    "Hall of Sacrilege": {"exits": [("Hallowed Hope", None)], "boss": "Golem"},
    "Advent Ground (South)": {"exits": [("Corridor of the Clerics", None), ("Passage of the Refugees (South)", None)]},
    "Passage of the Refugees (South)": {"exits": [("Advent Ground (South)", None), ("Passage of the Refugees (North)", "Hall of Sacrilege")]},
    "Passage of the Refugees (North)": {"exits": [("Passage of the Refugees (South)", "Hall of Sacrilege"), ("Advent Ground (North)", None)]},
    "Advent Ground (North)": {
        "exits": [("Passage of the Refugees (North)", None), ("The Cleansing Chantry", None)],
        "save_point": True,
        "container": True,
    },
    "The Cleansing Chantry": {"exits": [("Advent Ground (North)", None), ("Stairway to the Light", None)], "boss": "Dragon"},
    "Stairway to the Light": {"exits": [("The Cleansing Chantry", None), ("Rue Vermillion", None)]},
}
