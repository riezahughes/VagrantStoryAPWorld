room_data = {
    "The Dark Coast": {
        "exits": [("Tunnel of the Heartless", None), ("Hall of Prayer", None)],
        "save_point": True,
        "container": True,
        "traps": ["Trap Clear", "Heal Panel"],
    },
    "Hall of Prayer": {
        "exits": [("The Dark Coast", None), ("Those who Drink the Dark", None), ("The Resentful Ones", None)],
        "miniboss": "Last Crusader",
    },
    "Those who Drink the Dark": {
        "exits": [("Hall of Prayer", None), ("The Chapel of Meschaunce", None), ("Ants Prepare for Winter", "Silver Key")],
        "is_puzzle": True,
    },
    "The Chapel of Meschaunce": {"exits": [("Those who Drink the Dark", None)], "miniboss": "Minotaur Lord"},
    "The Resentful Ones": {"exits": [("Hall of Prayer", None), ("Those who Fear the Light", "Silver Key")], "is_puzzle": True},
    "Those who Fear the Light": {"exits": [("The Resentful Ones", None), ("Chamber of Reason", None)]},
    "Chamber of Reason": {"exits": [("Those who Fear the Light", None), ("Exit to City Center", None)], "boss": "Kali"},
    "Exit to City Center": {"exits": [("Chamber of Reason", None), ("Plateia Lumitar", None)]},
}
