room_data = {
    # --- IRON MAIDEN B2 ---
    "The Eunics' Lot": {"exits": [("Iron Maiden B1 Exit", None), ("Ordeal By Fire", None)]},
    "Ordeal By Fire": {"exits": [("The Eunics' Lot", None), ("The Oven at Neisse", None)]},
    "The Oven at Neisse": {"exits": [("Ordeal By Fire", None), ("Pressing", None)]},
    "Pressing": {"exits": [("The Oven at Neisse", None), ("The Mind Burns", None)]},
    "The Mind Burns": {"exits": [("Pressing", None), ("The Rack", None)]},
    "The Rack": {"exits": [("The Mind Burns", None), ("The Saw", None)]},
    "The Saw": {"exits": [("The Rack", None), ("The Cold's Bridle", None)]},
    "The Cold's Bridle": {"exits": [("The Saw", None), ("The Scavenger's Curse", None)]},
    "The Scavenger's Curse": {"exits": [("The Cold's Bridle", None), ("The Whack of Despair", None)]},
    "The Whack of Despair": {"exits": [("The Scavenger's Curse", None), ("The Dragging", None)]},
    "The Dragging": {"exits": [("The Whack of Despair", None), ("Ordeal by Water", None)]},
    "Ordeal by Water": {"exits": [("The Dragging", None), ("Tablillas", None), ("Strangulation", None)]},
    "Tablillas": {"exits": [("Ordeal by Water", None), ("The Strappado", None), ("Tormentum Insomniae", None)]},
    "Tormentum Insomniae": {
        "exits": [
            ("Tablillas", None),
            ("The Rack", None),
            ("The Iron Maiden", None),  # To B3 Boss
        ]
    },
}
