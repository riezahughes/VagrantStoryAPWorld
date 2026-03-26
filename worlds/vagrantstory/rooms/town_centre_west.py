room_data = {
    # --- TOWN CENTRE WEST ---
    "Rue Vermillion": {
        "exits": [
            ("Stairway to the Light", None),
            ("Tircolas Flow", None),
            ("The Rene Coastroad", None),
            ("Students of Death", "Crimson Key"),
        ]
    },
    "The Rene Coastroad": {
        "exits": [
            ("Rue Vermillion", None),
            ("Workshop 'Magic Hammer'", None),
            ("Rue Mal Fallde", None),
        ]
    },
    "Workshop 'Magic Hammer'": {
        "exits": [
            ("The Rene Coastroad", None),
        ]
    },
    "Rue Mal Fallde": {
        "exits": [
            ("The Rene Coastroad", None),
            ("Tircolas Flow", None),
        ]
    },
    "Tircolas Flow": {"exits": [("Rue Mal Fallde", None), ("Rue Vermillion", None)]},
    "Rue Bouquet": {
        "exits": [
            ("Tircolas Flow", None),
            ("Escapeway", None),
            ("Glacialdra Kirk Ruins", None),
        ]
    },
    "Glacialdra Kirk Ruins": {
        "exits": [
            ("Tircolas Flow", None),
            ("Rue Bouquet", None),
            ("Rue Sant D'alsa", None),
            ("Path to the Greengrocer", "Rood Inverse"),
        ]
    },
    "Rue Sant D'alsa": {
        "exits": [
            ("Glacialdra Kirk Ruins", None),
            ("Dinas Walk", None),
            ("Villeport Way", None),
        ]
    },
    "Dinas Walk": {
        "exits": [
            ("Rue Sant D'alsa", None),
            ("Villeport Way", None),
        ]
    },
    "Villeport Way": {
        "exits": [
            ("Dinas Walk", None),
            ("Rue Sant D'alsa", None),
            ("The Bread Peddler's Way", None),
        ]
    },
}
