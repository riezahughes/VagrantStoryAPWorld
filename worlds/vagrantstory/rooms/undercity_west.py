room_data = {
    # --- UNDERCITY WEST ---
    "The Bread Peddler's Way": {"exits": [("Villeport Way", None), ("Way of the Mother Lode", None)]},
    "Way of the Mother Lode": {"exits": [("The Bread Peddler's Way", None), ("Sewer of Ravenous Rats", None), ("Underdark Fishmarket", None)]},
    "Sewer of Ravenous Rats": {"exits": [("Way of the Mother Lode", None), ("Beggars of the Mouthharp", "Silver Key")]},
    "Underdark Fishmarket": {"exits": [("Way of the Mother Lode", None), ("The Sunless Way", None)]},
    "The Sunless Way": {
        "exits": [("Underdark Fishmarket", None), ("Dark Abhors Light", "Iron Key"), ("Remembering Days of Yore", None), ("Hall of Poverty", None)]
    },
    "Remembering Days of Yore": {"exits": [("The Sunless Way", None), ("Larder for a Lean Winter", "Iron Key"), ("Where the Hunter Climbed", None)]},
    "Larder for a Lean Winter": {"exits": [("Remembering Days of Yore", None)]},
    "Where the Hunter Climbed": {"exits": [("Remembering Days of Yore", None), ("The Faerie Circle", None)]},
    "Hall of Poverty": {"exits": [("The Sunless Way", None), ("The Washing-Woman's Way", None)]},
    "The Washing-Woman's Way": {"exits": [("Hall of Poverty", None), ("Nameless Dark Oblivion", "Silver Key")]},
    "Nameless Dark Oblivion": {"exits": [("The Washing-Woman's Way", "Silver Key"), ("Sinner's Corner", None)]},
    "Sinner's Corner": {
        "exits": [("Nameless Dark Oblivion", None), ("The Children's Hideout", None), ("Corner of Prayers", None), ("Fear of the Fall", None)]
    },
    "Fear of the Fall": {"exits": [("Sinner's Corner", None), ("The Cornered Savage", None)]},
    "The Children's Hideout": {"exits": [("Sinner's Corner", None)]},
    "Corner of Prayers": {"exits": [("Sinner's Corner", None), ("Hope Obstructed", None), ("Salvation for the Mother", "Gold Key")]},
    "Hope Obstructed": {"exits": [("Corner of Prayers", None), ("Work, Then Die", None)]},
    "Beggars of the Mouthharp": {"exits": [("Sewer of Ravenous Rats", "Silver Key"), ("Corner of the Wretched", None)]},
    "Corner of the Wretched": {"exits": [("Beggars of the Mouthharp", None), ("Crossroads of Rest", "Rood Inverse")]},
    "Crossroads of Rest": {"exits": [("Corner of the Wretched", "Rood Inverse"), ("Path to the Greengrocer", None), ("Path of the Children", None)]},
    "Path to the Greengrocer": {"exits": [("Crossroads of Rest", None), ("Glacialdra Kirk Ruins", "Rood Inverse")]},
    "Path of the Children": {"exits": [("Crossroads of Rest", None), ("Shelter From the Quake", None)]},
    "Salvation for the Mother": {
        "exits": [("Corner of Prayers", "Gold Key"), ("The Body Fragile Yields", "Gold Key"), ("Bite the Master's Wounds", None)]
    },
    "The Body Fragile Yields": {"exits": [("Tears from Empty Sockets", None), ("Salvation for the Mother", "Gold Key")]},
    "Bite the Master's Wounds": {"exits": [("Salvation for the Mother", None), ("Workshop 'Godhands'", None)]},
    "Workshop 'Godhands'": {"exits": [("Bite the Master's Wounds", None)]},
    "The Crumbling Market (South)": {"exits": [("Hall of Poverty", None), ("Tears from Empty Sockets", None), ("Subtellurian Horrors", None)]},
    "The Crumbling Market (North)": {"exits": [("Where Flood Waters Ran", None), ("The Crumbling Market (South)", None)]},
    "Where Flood Waters Ran": {"exits": [("The Crumbling Market (North)", None), ("The Darkness Drinks", None)]},
    "Tears from Empty Sockets": {"exits": [("The Body Fragile Yields", None), ("The Crumbling Market (South)", None), ("Rue Lejour", None)]},
}
