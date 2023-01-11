#!/usr/bin/python3
# This program checks the Users age and outputs the price of a game ticket

active = True
while active == True:
    name = input("Enter your name: ")
    age = input(f"What is your age {name}? : ")
    age = int(age)
    if age < 5:
        price = "Free"
    elif age < 18:
        price = 100
    elif age < 65:
        price = 300
    else:
        price = 150
    print(f"{name} your Total will be Ksh {price}")
    status = input("\nEnter 'quit' to exit the program else click Enter to proceed: " )
    if status != 'quit':
        continue
    else:
        active = False
        
    

