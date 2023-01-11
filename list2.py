#!/usr/bin/python3
# This file will demonstrate other methods of modifying using remove and pop 
starting_11 = []
starting_11.append("Ederson")
starting_11.append("Larpote")
starting_11.append("Akanji")
starting_11.append("Cancelo")
starting_11.append("Walker")
starting_11.append("Rodri")
starting_11.append("Gundogan")
starting_11.append("KDB")
starting_11.append("Foden")
starting_11.append("Sane")
starting_11.append("Haaland")

print(starting_11)
print("\n")

injured = starting_11.pop(4)
# We specified the element in the list to be removed (5) and moved the element to a new list
print(f"{injured}, was Injured duriung a training session\n")

print(starting_11)
# We can use remove when we want to remove an element permanently and won't re-use it but we don't know the position index
starting_11.remove("Sane")# An example of a Player who has transfered to another team was used in this case
print("\n")
print(starting_11)



