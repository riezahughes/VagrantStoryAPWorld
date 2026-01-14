room_data = {
    # --- TOWN CENTRE SOUTH ---
    "Forcas Rise": {
        "exits": [
            ("The Warrior's Rest", None),
            ("Valdiman Gates", None),
            ("Rue Aliano", None),
            ("Rue Faltes", None),
        ]
    },
    "Valdiman Gates": {
        "exits": [
            ("Forcas Rise", None),
            ("The Boy's Training Room", None),
        ]
    },
    "Rue Aliano": {
        "exits": [
            ("Forcas Rise", None),
            ("The House Khazabas", "Mandrake Sigil"),
        ]
    },
    "The House Khazabas": {
        "exits": [
            ("Rue Aliano", "Mandrake Sigil"),
            ("Zebel's Walk", None),
        ]
    },
    "Zebel's Walk": {
        "exits": [
            ("The House Khazabas", None),
            ("Rue Volnac", None),
        ]
    },
    "Rue Volnac": {
        "exits": [
            ("Zebel's Walk", None),
            ("Train and Grow Strong", None),
        ]
    },
    "Rue Faltes": {
        "exits": [
            ("Forcas Rise", None),
            ("Rue Morgue", None),
        ]
    },
    "Rue Morgue": {
        "exits": [
            ("Rue Faltes", None),
            ("Corridor of Shade", None),
        ]
    },
}
