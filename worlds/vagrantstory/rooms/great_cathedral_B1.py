room_data = {
    "Struggle for the Soul": {"exits": [("Into Holy Battle", None), ("Order and Chaos", None), ("Truth and Lies", None)], "traps": ["Heal Panel"]},
    "Order and Chaos": {"exits": [("Struggle for the Soul", None), ("An Offering of Souls", None)], "boss": "Marid"},
    "An Offering of Souls": {"exits": [("Order and Chaos", None), ("Sin and Punishment", None)]},
    "Truth and Lies": {"exits": [("Struggle for the Soul", None), ("Sanity and Madness", None), ("The Victor's Laurels", None)], "boss": "Ifrit"},
    "Sanity and Madness": {"exits": [("Truth and Lies", None)], "boss": "Iron Crab"},
    "The Victor's Laurels": {"exits": [("Truth and Lies", None), ("Cracked Pleasures", "Order and Chaos")]},
}
