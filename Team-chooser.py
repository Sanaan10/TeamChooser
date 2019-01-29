# Team-Chooser Program Created By Sanaan Wani
from random import choice
players = ['Sanaan', 'Huwaid', 'Mateen', 'Zooman', "Waseem", "Ikraam", "Hamza", "Souban", "Hadi", "Emaad"]
TeamA = []
TeamB = []
TeamC = []
while len(players) > 0:
    playerA = choice(players)
    print(playerA, "goes to TeamA", )
    TeamA.append(playerA)
    players.remove(playerA)
    print("Players Left:", players)
    print("Team A:", TeamA)
    print("Team B:", TeamB)
    print("Team C:", TeamC)

    if players == []:
        break
    playerB = choice(players)
    print(playerB,"goes to TeamB")
    TeamB.append(playerB)
    players.remove(playerB)
    if players == []:
        break
    playerC = choice(players)
    print(playerC,"goes to TeamC")
    TeamC.append(playerC)
    players.remove(playerC)
print("There you go, as fair as possible!")
