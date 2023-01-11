#!/usr/bin/python3
# More illustrations of Dictionaries

endorsements = {'Ederson' : 'Puma', 'Foden' : 'Nike', 'Alvarez' : 'Adidas', 'KDB' : 'Nike'}
print("The Following Brands have been picked by athletes")
for boot in endorsements.values():
    print(boot)
# We can use the values method to get only the values in the key pairs as shown above

# We can also get items not in the Dictionary
# Dybala has been seen wearing all blacked out boots which mostly means he is not endorsed and does not want to advertise for free
if 'Dybala' not in endorsements.keys():
    print("\nDybala is a Boot Free Agent!")

# .keys() works with particular items on the list
for name in sorted(endorsements.keys()):# Sorted sorts the list alphabetically
    print(f"\nThank you {name} for picking a Brand")

# Line 6 prints out the brands but one brand is repeated. we can counter this using the set method
print("\nThe Following Brands have endorsed athletes:")
for boot in set(endorsements.values()):
    print(boot)

# Sets are defined as follows
brands = {'Nike', 'Adidas', 'Puma', 'Nike', 'New Balance'}
print("\n")
print(brands)

