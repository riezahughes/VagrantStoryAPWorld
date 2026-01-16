room_data = {
    # --- CATACOMBS ---
    "Hall of Sworn Revenge": {
        "exits": [
            ("The Hero's Winehall", None),  # Connection to Wine Cellar
            ("The Last Blessing", None),
        ]
    },
    "The Last Blessing": {"exits": [("Hall of Sworn Revenge", None), ("The Weeping Corridor", None)]},
    "The Weeping Corridor": {"exits": [("The Last Blessing", None), ("Persecution Hall", None)]},
    "Persecution Hall": {"exits": [("The Weeping Corridor", None), ("Rodent-Ridden Chamber", None), ("Shrine to the Martyrs", None)]},
    "Rodent-Ridden Chamber": {"exits": [("Persecution Hall", None)]},
    "Shrine to the Martyrs": {"exits": [("Persecution Hall", None), ("The Lamenting Mother (West)", None), ("Hall of Dying Hope", None)]},
    "The Lamenting Mother (West)": {"exits": [("Shrine to the Martyrs", None)]},
    "The Lamenting Mother (East)": {"exits": [("The Last Stab of Hope", None)]},
    "Hall of Dying Hope": {"exits": [("Shrine to the Martyrs", None), ("Bandits' Hideout", None), ("The Bloody Hallway", None)]},
    "Bandits' Hideout": {"exits": [("Hall of Dying Hope", None)]},
    "The Bloody Hallway": {"exits": [("Hall of Dying Hope", None), ("Faith Overcame Fear", None)]},
    "Faith Overcame Fear": {"exits": [("The Bloody Hallway", None), ("The Withered Spring", None)]},
    "The Withered Spring": {
        "exits": [
            ("Faith Overcame Fear", None),
            ("Prisoners' Niche", "Lily Sigil"),  # Connection to Sanctum
            ("Workshop 'Work of Art'", None),
            ("Repent, O ye Sinners", None),
        ]
    },
    "Workshop 'Work of Art'": {"exits": [("The Withered Spring", None)]},
    "Repent, O ye Sinners": {"exits": [("The Withered Spring", None), ("The Reaper's Victims", None), ("The Last Stab of Hope", None)]},
    "The Reaper's Victims": {"exits": [("Repent, O ye Sinners", None)]},
    "The Last Stab of Hope": {"exits": [("Repent, O ye Sinners", None), ("The Lamenting Mother (East)", None), ("Hallway of Heroes", None)]},
    "Hallway of Heroes": {"exits": [("The Last Stab of Hope", None), ("The Beast's Domain", None)]},
    "The Beast's Domain": {"exits": [("Hallway of Heroes", None)]},
}
