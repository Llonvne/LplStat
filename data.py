status = [
    {
        "name": "BLG",
        "spring": 90,
        "summerRank": 1
    },
    {
        "name": "TES",
        "spring": 70,
        "summerRank": 3
    },
    {
        "name": "JDG",
        "spring": 50,
        "summerRank": 5
    },
    {
        "name": "NIP",
        "spring": 30,
        "summerRank": 9
    },
    {
        "name": "FPX",
        "spring": 20,
        "summerRank": 7
    },
    {
        "name": "WBG",
        "spring": 20,
        "summerRank": 4
    },
    {
        "name": "LNG",
        "spring": 10,
        "summerRank": 2
    },
    {
        "name": "AL",
        "spring": 0,
        "summerRank": 6
    },
    {
        "name": "TT",
        "spring": 0,
        "summerRank": 10
    },
    {
        "name": "LGD",
        "spring": 0,
        "summerRank": 8
    }
]

summerFinalRankScoreMap = {
    1: 200,
    2: 110,
    3: 80,
    4: 60,
    5: 40,
    6: 40,
    7: 10,
    8: 10,
    9: 0,
    10: 0
}

playoffs = {
    "G1": (8, 9),
    "G2": (7, 10),
    "G3": (5, "G1W"),
    "G4": (6, "G2W"),
    "G5": (3, "G3W"),
    "G6": (4, "G4W"),
    "G7": (1, "G5W"),
    "G8": (2, "G6W"),
    #     DOUBLE
    "G9": ("G7W", "G8W"),
    "G10": ("G7L", "G8L"),
    "G11": ("G9L", "G10W"),
    "G12": ("G9W", "G11W")
}
