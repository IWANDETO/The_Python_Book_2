#!/usr/bin/python3
# This file demonstrates the use of continue in Python
# This program prints out odd numbers within the given range
number = 0
while number < 100:
    number += 1
    if number % 2 == 0:
        continue # When continue is executed, the program returns to the beginning of the loop
    else:
        print(number)