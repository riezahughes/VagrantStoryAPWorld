room_data = {
    # --- ABANDONED MINES B2 ---
    "Subtellurian Horrors": {
        "exits": [
            ("The Crumbling Market (South)", None),  # Connection to Undercity West
            ("Dining in Darkness", None),
        ]
    },
    "Dining in Darkness": {"exits": [("Subtellurian Horrors", None), ("Bandit's Hollow", None)]},
    "Bandit's Hollow": {
        "exits": [
            ("Dining in Darkness", None),
            ("Delusions of Happiness", "Iron Key"),
            # Note: The one-way paths from 'The Lunatic Veins' and 'Work, Then Die'
            # only lead INTO this room, so they aren't listed as exits here.
        ]
    },
    "Delusions of Happiness": {"exits": [("Bandit's Hollow", None)]},
    "Work, Then Die": {
        "exits": [
            ("The Crossing", None),  # Connection to Undercity West
            ("Bandit's Hollow", None),  # One-way drop
            ("Rock Bottom", None),
        ]
    },
    "Rock Bottom": {"exits": [("Work, Then Die", None), ("Senses Lost", None)]},
    "Senses Lost": {"exits": [("Rock Bottom", None), ("Desire's Passage", None), ("The Lunatic Veins", None)]},
    "The Lunatic Veins": {
        "exits": [
            ("Senses Lost", None),
            ("Bandit's Hollow", None),  # One-way drop
        ]
    },
    "Desire's Passage": {"exits": [("Senses Lost", None), ("Way of Lost Children", None)]},
    "Way of Lost Children": {"exits": [("Desire's Passage", None), ("Treaty Room", None), ("Hidden Resources", None)]},
    "Hidden Resources": {"exits": [("Way of Lost Children", None)]},
    "Treaty Room": {"exits": [("Way of Lost Children", None), ("The Miner's End", None)]},
    "The Miner's End": {"exits": [("Treaty Room", None), ("Gambler's Passage", None)]},
    "Gambler's Passage": {"exits": [("The Miner's End", None), ("The Poor Man's Ward", None)]},
    "The Poor Man's Ward": {"exits": [("Gambler's Passage", None), ("Where Water Is Born", None)]},
    "Where Water Is Born": {"exits": [("The Poor Man's Ward", None), ("Hall of the Empty Bells", None)]},
    "Hall of the Empty Bells": {"exits": [("Where Water Is Born", None), ("Cul-de-Sac", None)]},
    "Cul-de-Sac": {
        "exits": [
            ("Hall of the Empty Bells", None),
            ("Forcas Rise", None),  # Connection to Town Centre South
        ]
    },
}
