#!/usr/bin/python3
# This program asks the user to input a number and tells the user if the number if odd or even
number = input("Enter a random number: ")
number = int(number)
if number % 2 == 0:
    print("\nThe Number you have entered is an Even Number!")
else:
    print("\nThe Number you have entered is an Odd Number!")