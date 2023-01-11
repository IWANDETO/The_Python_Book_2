#!/usr/bin/python3
# This program removes selected items in a list and prints out the remaining
brands = ['nike', 'adidas', 'puma', 'new balance', 'nike', 'new balance', 'adidas', 'new balance']
print(brands)
print("\n")
while 'new balance' in brands:
    brands.remove('new balance')

print(brands)