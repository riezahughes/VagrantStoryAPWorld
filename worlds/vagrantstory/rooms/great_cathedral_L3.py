room_data = {
    "The Wine-Lecher's Fall": {"exits": [("Free from Base Desires", None), ("The Heretics' Story (Lower)", None)]},
    "The Heretics' Story (Lower)": {"exits": [("The Wine-Lecher's Fall", None), ("Hopes of the Idealist", "Calla Sigil")]},
    "The Heretics' Story (Upper)": {
        "exits": [("The Heretics' Story (Lower)", None), ("Despair of the Fallen", None), ("Where the Soul Rots", "Light and Dark Wage War")]
    },
    "Despair of the Fallen": {"exits": [("The Heretics' Story (Upper)", "Maelstrom of Malice"), ("What Ails You, Kills You", None)]},
    "Hopes of the Idealist": {"exits": [("The Heretics' Story (Lower)", None)], "boss": "Dao"},
    "Where the Soul Rots": {"exits": [("The Heretics' Story (Upper)", None), ("The Atrium", None)]},
}
