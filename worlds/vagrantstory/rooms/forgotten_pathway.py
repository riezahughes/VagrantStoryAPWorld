room_data = {
    # --- FORGOTTEN PATHWAY ---
    "Stair to the Sinners": {
        "exits": [
            ("The Soldier's Bedding", None),  # To The Keep
            ("Slaugher of the Innocent", None),
        ]
    },
    "Slaughter of the Innocent": {"exits": [("Stair to the Sinners", None), ("The Oracle Sins No More", None)]},
    "The Oracle Sins No More": {"exits": [("Slaugher of the Innocent", None), ("The Fallen Knight", None), ("Awaiting Retribution", None)]},
    "The Fallen Knight": {"exits": [("The Oracle Sins No More", None)]},
    "Awaiting Retribution": {"exits": [("The Oracle Sins No More", None)]},
}
