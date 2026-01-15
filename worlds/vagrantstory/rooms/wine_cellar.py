room_data = {
    # --- WINE CELLAR ---
    "Entrance to Darkness": {"exits": [("Worker's Breakroom", None)]},
    "Worker's Breakroom": {"exits": [("Entrance to Darkness", None), ("Hall of Struggle", None)]},
    "Hall of Struggle": {"exits": [("Worker's Breakroom", None), ("Smokebarrel Stair", None)]},
    "Smokebarrel Stair": {"exits": [("Hall of Struggle", None), ("Wine Guild Hall", None), ("Room of Cheap Red Wine", "Chamomile Sigil")]},
    "Wine Guild Hall": {"exits": [("Smokebarrel Stair", None), ("Wine Magnate's Chambers", None)]},
    "Wine Magnate's Chambers": {"exits": [("Wine Guild Hall", None), ("Fine Vintage Vault", None)]},
    "Fine Vintage Vault": {"exits": [("Wine Magnate's Chambers", None), ("Chamber of Fear", None)]},
    "Chamber of Fear": {"exits": [("Fine Vintage Vault", None), ("The Reckoning Room", None), ("A Laborer's Thirst", None)]},
    "The Reckoning Room": {"exits": [("Chamber of Fear", None)]},
    "A Laborer's Thirst": {"exits": [("Chamber of Fear", None), ("The Rich Drown in Wine", None)]},
    "The Rich Drown in Wine": {"exits": [("A Laborer's Thirst", None), ("Room of Rotten Grapes", None)]},
    "Room of Rotten Grapes": {"exits": [("The Rich Drown in Wine", None), ("Blackmarket of Wines", None)]},
    "Blackmarket of Wines": {"exits": [("Room of Rotten Grapes", None), ("The Gallows", None)]},
    "The Gallows": {"exits": [("Blackmarket of Wines", None)]},
    "Room of Cheap Red Wine": {"exits": [("Smokebarrel Stair", None), ("Room of Cheap White Wine", None)]},
    "Room of Cheap White Wine": {"exits": [("Room of Cheap Red Wine", None), ("The Greedy One's Den", None)]},
    "The Greedy One's Den": {"exits": [("Room of Cheap White Wine", None), ("The Hero's Winehall", None)]},
    "The Hero's Winehall": {"exits": [("The Greedy One's Den", None), ("Hall of Sworn Revenge", None)]},
}

# """
#     For each room
#         create an exit
#         for each exit
#             create a requirement of "has item" if an item is specified
#         for each latch
#             create an entrance, not an exit.
# """
