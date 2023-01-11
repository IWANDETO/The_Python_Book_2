#!/usr/bin/python3
# This program moves items from one list to the other
unconfirmed_players = ['johnson', 'waldo', 'manu', 'jelle', 'ian', 'shakes', 'george', 'tony']
confirmed_players = []
while unconfirmed_players:
    player = unconfirmed_players.pop()

    print(f"Verifying: {player.title()}")
    confirmed_players.append(player)

print("\nThe following Players have been Verified: ")
for player in confirmed_players:
    print(player.title())