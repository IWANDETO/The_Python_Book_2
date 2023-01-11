#!/usr/bin/python3
# This file demonstrates the use of For loops in Python, which takes an action for every item on the list
players = ["Ederson","Ake", "Laporte","Dias", "Ortega", "Akanji","Stones","Cancelo","Walker", "Rodri", "Phillips","Gundogan", "Silva", "Foden", "Mahrez", "De Bruyne", "Alvarez", "Grealish", "Palmer", "Haaland"]
print("Manchester City Team Sheet:")
for player in players:
    print(player)
    # player is a temporay variable, representing singular form of players

# This for loop loops through every item and prints them out on the screen

for player in players:
    print(f"\nGood Game {player}.")
    print(f"Looking forward to your next game Mate!\n")

print("Come On City!")