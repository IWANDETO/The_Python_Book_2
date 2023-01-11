#!/usr/bin/python3
# This file demonstrates the use of Dictionaries in Python
# Lets create a dictionary to store attributes of a player
messi = {'Position' : 'CAM', 'Foot' : 'Left', 'Jersey' : 10, 'Strength' : 'Dribbling', 'Rating' : 90, }
print(messi)
# This dictionary defines key attributes of a player
print("\n")

# Lets create another dictionary entailing boot options for players
shoe_deal = {
    'Ederson' : 'Puma',
    'Haaland' : 'Adidas',
    'Foden' : 'Nike',
    'Sane' : 'Nike',
    'Alvarez' : 'Adidas',
    'KDB' : 'Nike',
    }
print(shoe_deal)

endorsement = shoe_deal['Haaland'].title()# This reassignment to a new variable makes it easy to print out
print(f"\nThe Viking is an {endorsement} Athlete!\n")# The Viking is prolific goal scorer Erling Haaland

# Leroy Sane is still endorsed by Nike, but he transferred to Bayern Munich
del shoe_deal['Sane']
print(shoe_deal)
# We deleted the Key Pair Sane since this shoe deal dictionary is based on City Players

# Now we can loop through the shoe deal dictionary
for athlete, shoe in shoe_deal.items():
    print(f"\nAthelete : {athlete}")
    print(f"Boot : {shoe}")
# We have created variables athlete and shoe to loop through all items in the dictionary

for athlete, shoe in shoe_deal.items():
    print(f"\n{athlete}'s favourite boots are {shoe}\n")
# The above is another demonstration of the for loop

"""athlete = ['KDB', 'Foden']
for athlete in shoe_deal:
    print(f"Hi {athlete}")

    if athlete in shoe_deal:
        shoe = shoe_deal{athlete}
        print(f"\nHi {athlete}, I see you like {shoe} Boots\n")"""

# We can use the get method to handle output for a key pair that is not available in the dictionary or deleted as shown below
player = shoe_deal.get('Sane', '\nPlayer Endorsement not available')
print(player)
print("\n")
# Creating an empty dictionary and adding info after

cr7 = {}
cr7['position'] = 'striking'
cr7['Foot'] = 'Right'
cr7['Jersey'] = 7
cr7['Strength'] = 'Attacking'
cr7['Rating'] = 90

print(cr7)

print("\n")

neymar = {}
neymar['position'] = 'LW'
neymar['Foot'] = 'Right'
neymar['Jersey'] = 10
neymar['Boots'] = 'Nike'
neymar['Rating'] = 90
print(neymar)
print("\n")
# We will modify one keypair in the dictionary Neymar
neymar['Boots'] = 'Puma'
print(f"Neymar is now wearing {neymar['Boots']} Boots \n")
# If you are a boot nerd like me, you are away that Nike dropped Neymar from their endorsed athletes and Puma signed him Up.

# I will use an if statement to increment the rating based on World Cup Perfomance
messi['Perfomance'] = 'Great'
if messi['Perfomance'] == 'Great':
    increment = 5
elif messi['Perfomance'] == 'Good':
    increment = 3
elif messi['Perfomance'] == 'Average':
    increment = 1
messi['Rating'] = messi['Rating'] + increment
print(f"Messi's New Fifa Rating is {messi['Rating']}.!\n")

cr7['Perfomance'] = 'Average'
if cr7['Perfomance'] == 'Great':
    increment = 5
elif cr7['Perfomance'] == 'Good':
    increment = 3
elif cr7['Perfomance'] == 'Average':
    increment = 1
cr7['Rating'] = cr7['Rating'] + increment
print(f"Ronaldo's New Fifa Rating is {cr7['Rating']}.!\n")

neymar['Perfomance'] = 'Good'
if neymar['Perfomance'] == 'Great':
    increment = 5
elif neymar['Perfomance'] == 'Good':
    increment = 3
elif neymar['Perfomance'] == 'Average':
    increment = 1
neymar['Rating'] = neymar['Rating'] + increment
print(f"Neymar's New Fifa Rating is {neymar['Rating']}.!\n")

# We have added a new keypair and assigned to each of the above three dictionaries
# We then used an if statement to determine the increment rating of each player based on the perfomance index
