#!/usr/bin/python3
# In this file, we will demonstrate the use of Tuples which contain immutable data
# Compared to lists, tuple are simpler data structures and use open and close parenthesis
dimensions = (200, 300)
print(dimensions)

# We cannot change the individual value of a tuple, however we can reassign the values to the variable
dimensions = (100, 150)
print(dimensions)

# We can also represent an individual value into a tuple but it will have to be followed by a comma
jersey_no = (10, )
print(jersey_no)