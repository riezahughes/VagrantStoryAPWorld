room_data = {
    "The Dark Coast": {"exits": [("Tunnel of the Heartless", None), ("Hall of Prayer", None)]},
    "Hall of Prayer": {
        "exits": [("The Dark Coast", None), ("Those who Drink the Dark", None), ("The Resentful Ones", None)],
    },
    "Those who Drink the Dark": {
        "exits": [("Hall of Prayer", None), ("The Chapel of Meschaunce", None), ("Ants Prepare for Winter", "Silver Key")],
    },
    "The Chapel of Meschaunce": {
        "exits": [("Those who Drink the Dark", None)],
    },
    "The Resentful Ones": {"exits": [("Hall of Prayer", None), ("Those who Fear the Light", "Silver Key")]},
    "Those who Fear the Light": {"exits": [("The Resentful Ones", "Silver Key"), ("Chamber of Reason", None)]},
    "Chamber of Reason": {"exits": [("Those who Fear the Light", None), ("Exit to City Center", None)]},
    "Exit to City Center": {"exits": [("Chamber of Reason", None), ("Plateia Lumitar", None)]},
}
