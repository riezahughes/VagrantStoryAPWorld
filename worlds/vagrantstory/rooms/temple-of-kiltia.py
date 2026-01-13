room_data = {
    "The Dark Coast": {
        "exits": [
            ("Tunnel of the Heartless", None),  # To Limestone Quarry
            ("Hall of Prayer", None),
        ]
    },
    "Hall of Prayer": {"exits": [("The Dark Coast", None), ("Those who Drink the Dark", None), ("The Resentful Ones", None)]},
    "Those who Drink the Dark": {
        "exits": [
            ("Hall of Prayer", None),
            ("The Chapel of Meschaunce", None),
            ("Ants Prepare for Winter", "Silver Key"),  # To Limestone Quarry
        ]
    },
    "The Resentful Ones": {"exits": [("Hall of Prayer", None), ("Those who Fear the Light", "Silver Key")]},
    "Those who Fear the Light": {"exits": [("The Resentful Ones", None), ("Chamber of Reason", None)]},
}
