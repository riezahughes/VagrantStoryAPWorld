room_data = {
    # --- THE KEEP ---
    "The Soldier's Bedding": {
        "exits": [
            ("The Boy's Training Room", None),  # To City Walls South
            ("A Storm of Arrows", None),
            ("Stair to the Sinners", "Gold Key"),  # To Forgotten Pathway
            ("The Cage", None),  # To Iron Maiden B1
        ]
    },
    "A Storm of Arrows": {
        "exits": [
            ("The Soldier's Bedding", None),
            ("Urge the Boy On", None),
            ("Time Trial (Minotaur)", "Kalmia Sigil"),
            ("Time Trial (Dragon)", "Columbine Sigil"),
        ]
    },
    "Time Trial (Minotaur)": {"exits": [("A Storm of Arrows", None)]},
    "Time Trial (Dragon)": {"exits": [("A Storm of Arrows", None)]},
    "Urge the Boy On": {
        "exits": [
            ("A Storm of Arrows", None),
            ("A Taste of the Spoils", None),
            ("Time Trial (Earth Dragon)", "Anemone Sigil"),
            ("Time Trial (Snow Dragon)", "Verbena Sigil"),
        ]
    },
    "Time Trial (Earth Dragon)": {"exits": [("Urge the Boy On", None)]},
    "Time Trial (Snow Dragon)": {"exits": [("Urge the Boy On", None)]},
    "A Taste of the Spoils": {
        "exits": [
            ("Urge the Boy On", None),
            ("Wiping Blood from Blades", None),
            ("Time Trial (Damascus Golem)", "Schirra Sigil"),
            ("Time Trial (Damascus Crab)", "Marigold Sigil"),
        ]
    },
    "Time Trial (Damascus Golem)": {"exits": [("A Taste of the Spoils", None)]},
    "Time Trial (Damascus Crab)": {"exits": [("A Taste of the Spoils", None)]},
    "Wiping Blood from Blades": {
        "exits": [
            ("A Taste of the Spoils", None),
            ("The Warrior's Rest", None),
            ("Time Trial (Death + Ogre Zombie)", "Azalea Sigil"),
            ("Time Trial (Asura)", "Tigertail Sigil"),
        ]
    },
    "Time Trial (Death + Ogre Zombie)": {"exits": [("Wiping Blood from Blades", None)]},
    "Time Trial (Asura)": {"exits": [("Wiping Blood from Blades", None)]},
    "The Warrior's Rest": {
        "exits": [
            ("Wiping Blood from Blades", None),
            ("Workshop 'Keane's Crafts'", None),
            ("Forcas Rise", None),  # To Town Centre South
        ]
    },
    "Workshop 'Keane's Crafts'": {"exits": [("The Warrior's Rest", None)]},
}
