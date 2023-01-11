#!/usr/bin/python3
# You can create an empty list then add elements to it
# This file will demonstrate the various methods of modifying lists in Python
cars_brands = []
cars_brands.append("BMW")
print(cars_brands)
cars_brands.append("Toyota")
cars_brands.append("Land Rover")
cars_brands.append("Mercedes")
cars_brands.append("Honda")

print(cars_brands)
# You can also add an element in the list using insert to a given index which will move the elements in that position one step to the right
cars_brands.insert(0, "Audi")
print(cars_brands)

# You can delete individual elements in the list using the del function
del cars_brands[5]
print(cars_brands)
