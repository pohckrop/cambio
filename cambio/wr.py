import numpy as np
import scipy as sp
import random


players = {
    "1": 1000,
    "2": 1000
}

winrates = {
    "Gianna": 0.836,
    "Joe": 0.678,
    "Emma Yin": 0.811,
    "Mia": 0.569,
    "Matt": 0.557,
    "Bryant": 0.637,
    "Riku": 0.495,
    "Anna": 0.525,
    "Ellen": 0.594,
    "Elizabeth": 0.450,
    "Evelynn": 0.431,
    "Adam": 0.478,
    "Joan": 0.446,
    "Mira": 0.405,
    "Harper": 0.446,
    "Humberto": 0.223,
    "Abhinav": 0.279,
    "Serena": 0.203,
    "Catherine": 0.186,
    "Ishan": 0.131,
    "Michael": 0,
    "Nipun": 0,
    "Rory": 0,
    "Ainsley": 0
}

def elo(players, winner, K=16):
    add = 0
    for opponent in players:
        if opponent == winner:
            continue

        Ra = players[winner]
        Rb = players[opponent]

        Ea = 1 / (1 + 10 ** ((Rb - Ra) / 400))
        Eb = 1 - Ea

        add += K * (1 - Ea)
        players[opponent] += K * (0 - Eb)

    players[winner] += add
    return players


total = 0

for name, wr in winrates.items():
    total = 0

    for experiment in range(100):

        # reset Elo each experiment
        players["1"] = 1000
        players["2"] = 1000

        for game in range(10000):
            if random.random() < wr:
                elo(players, "1")
            else:
                elo(players, "2")
                
            

        total += players["1"]

    print(name, "avg Elo:", total / 100)


