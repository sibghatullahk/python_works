players=['kjaer', 'Maxx', 'bob', 'john', 'eli', 'virg', 'eze']
print(players[0:3])
print(players[1:4])
print(players[:5])
print(players[3:])
print(players[0:6:2])
print("Here are the first three players in the game")
for player in players[0:3]:
    print(player.title())