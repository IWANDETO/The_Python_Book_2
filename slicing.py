#!/usr/bin/python3
# This file will demonstrate the use of Slicing Lists in Python
# Note the one of rule still applies in the case where the value of the second digit will not be printed
players = ["Ederson","Ake", "Laporte","Dias", "Ortega", "Akanji","Stones","Cancelo","Walker", "Rodri", "Phillips","Gundogan", "Silva", "Foden", "Mahrez", "De Bruyne", "Alvarez", "Grealish", "Palmer", "Haaland"]

print(players[0:3])
print("\n")

# Generating a subset
print(players[2:7])
print("\n")

# Omitting the last index results with the last index being printed out starting from the specified index
print(players[9:])
print("\n")

# Omitting the first index results with the first index being printed out up-to the second last digit of the specified
print(players[:5])
print("\n")

# Printing from the last index using the negative sign is also possible as demonstrated below
print(players[-4:])
print("\n")

# Lastly we will loop through using the slicing method
print("This are the first three players:\n")
for player in players[:3]:
    print(player)