room_data = {
    "Shelter From the Quake": {
        "exits": [("Path of the Children", None), ("Buried Alive", "Gold Key"), ("Movement of Fear", "Silver Key"), ("Fear and Loathing", None)]
    },
    "Buried Alive": {"exits": [("Shelter From the Quake", None)], "enemy": "Fire Elemental"},
    "Movement of Fear": {"exits": [("Shelter From the Quake", None), ("Facing Your Illusions", None)], "enemy": "Air Elemental"},
    "Facing Your Illusions": {"exits": [("Movement of Fear", None), ("The Darkness Drinks", None)], "traps": ["Diabolos"]},
    "The Darkness Drinks": {"exits": [("Facing Your Illusions", None), ("Where Flood Waters Ran", None)], "enemy": "Earth Elemental"},
    "Fear and Loathing": {"exits": [("Shelter From the Quake", None), ("Blood and The Beast", None)], "minibosses": ["Ifrit", "Marid"]},
    "Blood and The Beast": {
        "exits": [("Fear and Loathing", None), ("Where Body and Soul Part", None)],
        "traps": ["Poison Panel"],
        "enemy": "Water Elemental",
    },
    "Where Body and Soul Part": {"exits": [("Blood and The Beast", None)], "notes": "Chest is warded."},
}
