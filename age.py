#!/usr/bin/python3
# This Program checks if a person is old enough to Vote
name = input("What is your name: ")

age = input(f"\nHow Old are you {name}? : ")
age = int(age)
if age >= 18:
    print(f"\nCongradulations {name}! You can register for a Voters card.")
else:
    print(f"\nUnfortunately {name} you are too young to Vote, come back when you turn 18.")