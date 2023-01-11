#!/usr/bin/python3
# Being a football fan, I generally use that knownlegde to come up with scenarios to suite a code fucntionality demo
# The below list entails items of a Brand, case-point Nike which are in stock
available_gear = ["Boots", "Socks", "Shin Guards", "Shorts", "Jersey", "Wrist Band", "Body Amour"]
# Now lets make a list of items that a customer wants
requested_gear = ["Boots", "Socks", "Shin Guards", "Shorts", "Jersey", "Head Band", "Ankle Tape"]
# Now lets compare the two lists
for requested_gear in requested_gear:
    if requested_gear in available_gear:
        print(f"Adding {requested_gear} to your Gear.")
    else:
        print(f"Sorry, we do not have {requested_gear} in our collection")
print("\nYour Gear has been assembled Player!\n")

# We can also check to see if a list is empty
requested_gear = []
if requested_gear:
    for requested_gear in requested_gear:
        print(f"Adding {requested_gear} to your gear")
    print("\nYour Gear has been assembled player!")
else:
    print("\nAre you sure you don't want any Gear?")
