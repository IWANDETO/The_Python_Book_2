#!/usr/bin/python3
# This file demonstrates creating a dictionary in another dictionary

messi = {'Position' : 'CAM', 
    'Foot' : 'Left', 
    'Jersey' : 10, 
    'Strength' : 'Dribbling', 
    'Rating' : 90, 
    }

cr7 = {'position' : 'striking',
    'Foot' : 'Right',
    'Jersey' : 7,
    'Strength' : 'Attacking',
    'Rating' : 90,
    }



neymar = {'position' : 'LW',
    'Foot' : 'Right',
    'Jersey' : 10,
    'Boots' : 'Nike',
    'Rating' : 90,
    }

nominees = [messi , cr7 ,neymar]
for nominee in nominees:
    print(nominee)

# Let us create a list of dictionaries simultaneously
players = [] # First we create a list of players called players
for player_no in range(11):
    player = {'player' : 'Name', 'Jersey' : '10', 'Position' : 'Striking'}
    players.append(player)

# Let us print out the new list
for player in players:
    print(player)
print(f"\nNumber of players is: {len(players)}\n")

# Let us modify the items in the Dictionaries using If statements

for player in players[:4]:
    if player['Position'] == 'Striking':
     player['Position'] = 'Defender'
    print(player)
for player in players[4:7]:
    if player['Position'] == 'Striking':
        player['Position'] = 'Midfielder'
        print(player)
for player in players[7:10]:
    if player['Position'] == 'Striking':
        player['Position'] = 'Striker'
        print(player)
for player in players[:11]:
    if player['Position'] == 'Striking':
        player['Position'] = 'Goalkeeper'
        print(player)


# Lists in a Dictionary
# We can create a list inside a Dictionary to display different values at the same time

shoe = {
    'brand' : 'Nike',
    'features' : ['All Climate Control', 'Lacesless'],
}

print(f"\nYou have ordered a {shoe['brand']} "
        "with the following Features:")# We can break the line and tab. Python will still combine the string
for feature in shoe['features']:
    print(f"\t{feature}")
# Key pair Feature contains a list inside it

accessories = {
    'Mahrez' : ['Gloves', 'Mavin', 'Wrist Bands'],
    'Grealish' : ['Kids Shin Guards', 'Short Pair of Socks'],
    'Foden' : ['Body Armour', 'Compression Shorts'],
    'Lewis' : ['Head Bands', 'Soccer Vest'],
}
for name, accessory in accessories.items():
    print(f"\n{name} has requested the Special Items as below: ")
    for accessory in accessory:
        print(accessory)

# Dictionaries in dictionaries
# We can store a dictionary inside a dictionary but not that it can get complex quickly

players = {
    'Mahrez' : {
        'first' : 'Riyad',
        'second' : 'Mahrez',
        'position' : ['Right Wing', 'Left Wing'], 
        'Jersey' : 26,
    },

     'Cancelo' : {
        'first' : 'Joao',
        'second' : 'Cancelo',
        'position' : ['Right Back', 'Left Back'],
        'Jersey' : 7,
    },

     'Haaland' : {
        'first' : 'Erling',
        'second' : 'Haaland',
        'position' : 'Striker',
        'Jersey' : 9,
    },

     'Walker' : {
        'first' : 'Kyle',
        'second' : 'Walker',
        'position' : 'Right Back',
        'Jersey' : 2,
    },

     'Ederson' : {
        'first' : 'Ederson',
        'second' : 'Moraes',
        'position' : 'Goal Keeper',
        'Jersey' : 31,
    }

}

for player, player_info in players.items():
    print(f"\nPlayer Name: {player}")
    full_name = f"{player_info['first']} {player_info['second']}"
    position = player_info['position']
    jersey = player_info['Jersey']

    print(f"Full Name: {full_name}")
    print(f"Position: {position}")
    print(f"Jersey No: {jersey}\n")