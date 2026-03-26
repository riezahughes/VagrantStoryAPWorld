room_data = {
    "Free from Base Desires": {"exits": [("Cracked Pleasures", None), ("Abasement from Above", None), ("The Wine-Lecher's Fall", None)]},
    "Abasement from Above": {"exits": [("Free from Base Desires", None), ("The Convent Room", None), ("The Hall of Broken Vows", None)]},
    "The Convent Room": {"exits": [("Into Holy Battle", None)]},
    "The Hall of Broken Vows": {
        "exits": [
            ("Abasement from Above", None),
            ("The Melodics of Madness", "Acacia Sigil"),
            ("He Screams for Mercy", None),
            ("Light and Dark Wage War", None),
        ],
    },
    "Light and Dark Wage War": {"exits": [("The Hall of Broken Vows", None), ("An Arrow into Darkness", None)]},
    "An Arrow into Darkness": {"exits": [("Light and Dark Wage War", None), ("Where Darkness Spreads", None)]},
    "He Screams for Mercy": {"exits": [("The Hall of Broken Vows", None), ("Maelstrom of Malice", None), ("The Acolyte's Weakness", None)]},
    "The Acolyte's Weakness": {"exits": [("He Screams for Mercy", None), ("Monk's Leap", None)]},
    "Maelstrom of Malice": {"exits": [("He Screams for Mercy", None)]},
    "The Melodics of Madness": {"exits": [("The Hall of Broken Vows", "Acacia Sigil"), ("What Ails You, Kills You", "Palm Sigil")]},
    "What Ails You, Kills You": {"exits": [("The Melodics of Madness", "Palm Sigil"), ("Despair of the Fallen", None)]},
}
