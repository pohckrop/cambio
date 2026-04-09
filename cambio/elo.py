import numpy as np
import scipy as sp
import random
import matplotlib.pyplot as plt

#enter players here + elos
players = {
    "Mia": 1021,
    "Matt": 1019,
    "Humberto": 890,
    "Elizabeth": 992,
    "Joe": 1062,
    "Abhinav": 909,
    "Eve": 973
}

def elo_multiplayer(players, winner, K=24):
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

#select winners here
#if n-way ties, divide K by n and run n times

elo_multiplayer(players, "Mia")
elo_multiplayer(players, "Joe")
#elo_multiplayer(players, "")
#elo_multiplayer(players, "")
#elo_multiplayer(players, "")
#elo_multiplayer(players, "")
#elo_multiplayer(players, "")
#elo_multiplayer(players, "")
#elo_multiplayer(players, "")
#elo_multiplayer(players, "")

print("New Elos:")
for i in players:
    print(i, ":", players[i])
