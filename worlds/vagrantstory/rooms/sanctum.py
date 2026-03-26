room_data = {
    "Prisoners' Niche": {"exits": [("The Withered Spring", "Lily Sigil"), ("Corridor of the Clerics", None)]},
    "Corridor of the Clerics": {
        "exits": [("Prisoners' Niche", None), ("Priests' Confinement", None), ("Advent Ground", None), ("The Academia Corridor", None)]
    },
    "Priests' Confinement": {"exits": [("Corridor of the Clerics", None), ("Alchemists' Laboratory", None)]},
    "Alchemists' Laboratory": {"exits": [("Priests' Confinement", None), ("The Academia Corridor", None)]},
    "The Academia Corridor": {
        "exits": [("Corridor of the Clerics", None), ("Theology Classroom", None), ("Shrine of the Martyrs", None), ("Alchemists' Laboratory", None)],
    },
    "Theology Classroom": {"exits": [("The Academia Corridor", None)]},
    "Shrine of the Martyrs": {"exits": [("The Academia Corridor", None), ("Hallowed Hope", None)]},
    "Hallowed Hope": {"exits": [("Shrine of the Martyrs", None), ("Hall of Sacrilege", None)]},
    "Hall of Sacrilege": {"exits": [("Hallowed Hope", None)]},
    "Advent Ground": {"exits": [("Corridor of the Clerics", None), ("Passage of the Refugees", None), ("The Cleansing Chantry", None)]},
    "Passage of the Refugees": {"exits": [("Advent Ground", None)]},
    "The Cleansing Chantry": {"exits": [("Advent Ground", None), ("Stairway to the Light", None)]},
    "Stairway to the Light": {"exits": [("The Cleansing Chantry", None), ("Rue Vermillion", None)]},
}
