#!/usr/bin/python3
# This file demonstrates the use of if statements in Python
cars = ['bmw', 'audi', 'toyota', 'mercedes', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# If you are a car enthusiast like me, you surely know that BMW is most often than not written in uppercase.
# The above code checks if the car is a BMW and converts it into Uppercase as the brand name and prints out the rest in title case

# We can also convert the values to lowercase to check the value regardless it being upper or lower case
names = ['Michael', 'Dwight', 'Pam', 'Jim', 'Angela']
for name in names:
    if name.lower() == 'jim':
        print("\nJim is present in The Office today")

# We can also do a not equal to comparison
requested_salesman = 'Dwight'
for name in names:
    if name.lower() != 'dwight':
        print("\nHold on the Line, Dwight will answer your call shortly.")
    else:
        print(f"\n{name} Shrute speaking.")

# We can also use the comparison statements with numbers
age = 17
if age != 18:
    print("\nYou are not yet eligible for a National ID")
if age >= 18:
    print("You can apply for an Internship at the Office")
else:
    print("You are too young to work here.")

age = 18
if age == 18:
    print("\nYou can proceed to apply for a National ID")

if age >= 18:
    print("You can apply for an Internship at the Office")
else:
    print("You are too young to work here.")

# Using AND and OR
age = 18
year_of_study = 3
if (age >= 18) and (year_of_study >= 2):#Both tests must be true to execute the statement following
    print("\nYou can apply for an attachment program")
else:
    print("\nYou are not yet eligible to go for an attachment program")

has_id = False
has_passport = True
if (has_id == True ) or (has_passport == True):#Checks if at least one condition is true and executes the code below it
    print("\nYou can vote in the upcoming election")
else:
    print("\nYou cannot vote without an ID or Passport")

# We can also check if the value exists in a list
fpl_team = ["De Bruyne", "Salah", "Martinez", "Rashford"]
player = "Haaland"
if player not in fpl_team:
    fpl_team.append(player)
    print(f"\n{player} has been added to your squad")
if "Haaland" in fpl_team:
    fpl_captain = "Haaland"
    print("You Captain of the squad is Haaland!")

# We can add a Boolean Value
game_week_active = True

