room_data = {
    "Free from Base Desires": {"exits": [("Cracked Pleasures", None), ("Abasement from Above", None), ("The Wine-Lecher's Fall", None)]},
    "Abasement from Above": {
        "exits": [("Free from Base Desires", None), ("The Convent Room", None), ("The Hall of Broken Vows", None)],
        "traps": ["Poison Panel", "Paralysis Panel", "Curse Panel"],
    },
    "The Convent Room": {"exits": [("Into Holy Battle", None)]},
    "The Hall of Broken Vows": {
        "exits": [
            ("Abasement from Above", None),
            ("The Melodics of Madness", "Acacia Sigil"),
            ("He Screams for Mercy", None),
            ("Light and Dark Wage War", None),
        ],
        "miniboss": "Flame Dragon",
    },
    "Light and Dark Wage War": {"exits": [("The Hall of Broken Vows", None), ("An Arrow into Darkness", None)]},
    "An Arrow into Darkness": {"exits": [("Light and Dark Wage War", None), ("Where Darkness Spreads", None)]},
    "He Screams for Mercy": {
        "exits": [("The Hall of Broken Vows", None), ("Maelstrom of Malice", None), ("The Acolyte's Weakness", None)],
        "traps": ["Terra Thrust", "Cure Panel"],
    },
    "The Acolyte's Weakness": {"exits": [("He Screams for Mercy", None), ("Monk's Leap", None)]},
    "Maelstrom of Malice": {"exits": [("He Screams for Mercy", None)], "miniboss": "Lich Lord"},
    "The Melodics of Madness": {"exits": [("The Hall of Broken Vows", None), ("What Ails You, Kills You", "Palm Sigil")]},
    "What Ails You, Kills You": {"exits": [("The Melodics of Madness", None), ("Despair of the Fallen", None)], "boss": "Nightmare"},
}
