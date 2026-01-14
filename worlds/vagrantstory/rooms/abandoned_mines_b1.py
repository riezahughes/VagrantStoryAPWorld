room_data = {
    # --- ABANDONED MINES B1 ---
    "Dreamers' Entrance": {"exits": [("Where the Master Fell", None), ("The Crossing", None)]},
    "The Crossing": {
        "exits": [("Dreamers' Entrance", None), ("Miners' Resting Hall", None), ("Conflict and Accord", None), ("The Suicide King", None)]
    },
    "Miners' Resting Hall": {"exits": [("The Crossing", None)]},
    "Conflict and Accord": {"exits": [("The Crossing", None), ("The End of the Line", None)]},
    "The End of the Line": {"exits": [("Conflict and Accord", None), ("The Earthquake's Mark", None)]},
    "The Earthquake's Mark": {
        "exits": [
            ("The End of the Line", None),
            ("Coal Mine Storage", None),
            ("The Passion of Lovers", "Hyacinth Sigil"),
            # Note: The West exit to 'Fruits of Friendship' is a latch,
            # so it is not listed here as a reachable exit.
        ]
    },
    "Coal Mine Storage": {"exits": [("The Earthquake's Mark", None)]},
    "The Suicide King": {"exits": [("The Crossing", None), ("The Battle's Beginning", None)]},
    "The Battle's Beginning": {"exits": [("The Suicide King", None), ("What Lies Ahead?", None)]},
    "What Lies Ahead?": {"exits": [("The Battle's Beginning", None), ("The Fruits of Friendship", None)]},
    "The Fruits of Friendship": {
        "exits": [
            ("What Lies Ahead?", None),
            ("The Earthquake's Mark", None),  # This allows the latch to be opened from this side
        ]
    },
    "The Passion of Lovers": {"exits": [("The Earthquake's Mark", None), ("The Hall of Hope", None)]},
    "The Hall of Hope": {"exits": [("The Passion of Lovers", None), ("The Dark Tunnel", None)]},
    "The Dark Tunnel": {"exits": [("The Hall of Hope", None), ("Everwant Passage", None), ("Rust in Peace", None), ("The Smeltry", None)]},
    "Everwant Passage": {"exits": [("The Dark Tunnel", None), ("Mining Regrets", "Silver Key")]},
    "Mining Regrets": {"exits": [("Everwant Passage", None)]},
    "Rust in Peace": {"exits": [("The Dark Tunnel", None)]},
    "The Smeltry": {"exits": [("The Dark Tunnel", None), ("Clash of Hyaenas", None)]},
    "Clash of Hyaenas": {"exits": [("The Smeltry", None), ("Greed Knows No Bounds", None)]},
    "Greed Knows No Bounds": {"exits": [("Clash of Hyaenas", None), ("Live Long and Prosper", None)]},
    "Live Long and Prosper": {"exits": [("Greed Knows No Bounds", None), ("Pray to the Mineral Gods", "Fern Sigil")]},
    "Pray to the Mineral Gods": {"exits": [("Live Long and Prosper", None), ("Traitor's Parting", None)]},
    "Traitor's Parting": {"exits": [("Pray to the Mineral Gods", None), ("Escapeway", None)]},
    "Escapeway": {"exits": [("Traitor's Parting", None), ("Rue Bouquet", None)]},
}
