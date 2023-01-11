#!/usr/bin/python3
# This file demonstrates copying lists in Python basically using the slicing principle
epl_players = ["Ederson","Ake", "Laporte","Dias", "Ortega", "Akanji","Stones","Cancelo","Walker", "Rodri", "Phillips","Gundogan", "Silva", "Foden", "Mahrez", "De Bruyne", "Grealish", "Haaland"]
ucl_players = epl_players[:]
print("This are players available for the Premier League:")
print(epl_players)

print("\nThis are players available for the Uefa Champions League:")
print(ucl_players)
# Both lists printed out contain the same values

# To show that despite having the same values these lists are indeed different, we will append the lists
epl_players.append("Palmer")
print("This are players available for the Premier League:")
print(epl_players)

ucl_players.append("Alvarez")
print("\nThis are players available for the Uefa Champions League:")
print(ucl_players)
# The output now shows the different outcomes entailing values that have been added to the lists