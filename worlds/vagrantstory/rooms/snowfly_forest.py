room_data = room_data = {
    "The Faerie Circle": {"exits": [("Where the Hunter Climbed", None), ("The Hunt Begins", None)], "save_point": True},
    "The Hunt Begins": {"exits": [("The Faerie Circle", None), ("Which Way Home", None)]},
    "Which Way Home": {
        "exits": [("The Hunt Begins", None), ("The Giving Trees", None), ("The Wounded Boar", None), ("The Birds and the Bees", None)]
    },
    "The Giving Trees": {"exits": [("Which Way Home", None), ("The Spirit Trees", None), ("They Also Feed", None)]},
    "The Birds and the Bees": {
        "exits": [("Which Way Home", None), ("They Also Feed", None), ("The Giving Trees", None), ("Traces of the Beast", None)]
    },
    "The Wounded Boar": {"exits": [("Which Way Home", None), ("Golden Egg Way", None)]},
    "Golden Egg Way": {"exits": [("The Wounded Boar", None), ("Traces of the Beast", None), ("Fluttering Hope", None), ("The Yellow Wood", None)]},
    "Traces of the Beast": {
        "exits": [("The Birds and the Bees", None), ("Fluttering Hope", None), ("The Yellow Wood", None), ("Golden Egg Way", None)]
    },
    "Fluttering Hope": {"exits": [("Traces of the Beast", None), ("Golden Egg Way", None), ("Return to the Land", None)]},
    "Return to the Land": {"exits": [("Fluttering Hope", None), ("The Spirit Trees", None)], "boss": "Earth Dragon"},
    "The Yellow Wood": {
        "exits": [("Traces of the Beast", None), ("Golden Egg Way", None), ("Where Soft Rains Fell", "Return to the Land"), ("They Also Feed", None)]
    },
    "They Also Feed": {
        "exits": [("The Yellow Wood", None), ("The Giving Trees", None), ("The Birds and the Bees", None), ("The Spirit Trees", None)]
    },
    "The Spirit Trees": {"exits": [("They Also Feed", None), ("The Giving Trees", None)]},
    "Where Soft Rains Fell": {"exits": [("The Yellow Wood", "Return to the Land"), ("Forest River", None)]},
    "Forest River": {
        "exits": [("Where Soft Rains Fell", None), ("The Faerie Circle", None), ("Lamenting to the Moon", None)],
        "save_point": True,
        "traps": ["Cure Panel"],
    },
    "Lamenting to the Moon": {
        "exits": [("Forest River", None), ("The Wolves' Choice", None), ("Howl of the Wolf King", None), ("Running with the Wolves", None)]
    },
    "Running with the Wolves": {"exits": [("Lamenting to the Moon", None), ("The Hollow Hills", None), ("You Are the Prey", None)]},
    "You Are the Prey": {
        "exits": [("Running with the Wolves", None), ("The Secret Path", None), ("The Silent Hedges", None), ("The Hollow Hills", None)]
    },
    "The Secret Path": {"exits": [("You Are the Prey", None), ("Hewn from Nature", None)]},
    "Hewn from Nature": {"exits": [("The Secret Path", None), ("The Wood Gate", None)], "bosses": ["Grissom", "Dark Crusader"]},
    "The Wood Gate": {"exits": [("Hewn from Nature", None), ("The Weeping Boy", None)], "save_point": True},
    "The Wolves' Choice": {
        "exits": [("Golden Egg Way", None), ("The Woodcutter's Run", None), ("Howl of the Wolf King", None), ("They Also Feed", None)]
    },
    "The Woodcutter's Run": {"exits": [("The Birds and the Bees", None), ("The Wolves' Choice", None), ("The Yellow Wood", None)]},
    "The Hollow Hills": {"exits": [("Running with the Wolves", None), ("Howl of the Wolf King", None)]},
    "Howl of the Wolf King": {"exits": [("The Hollow Hills", None), ("Lamenting to the Moon", None), ("The Silent Hedges", None)]},
    "The Silent Hedges": {"exits": [("Lamenting to the Moon", None), ("The Spirit Trees", None)]},
}
