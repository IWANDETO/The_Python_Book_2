#!/usr/bin/python3
# Range function can be used to generate variety of lists while working with numbers
for value in range(1, 10):
    print(value)
# When we run the above code, a range of numbers from 1 to 9 is printed out and 10 is excluded following the one-off rule in programming

print("\n")

# We can also create a list by using the list and range function together
value = list(range(1, 10))
print(value)
# value is now printed as a list

print("\n")

# When we pass a third argument, range uses the value as a step size
even_numbers = list(range(2, 10, 2))
print(even_numbers)

print("\n")

# Using for loops with range
squares = []
for value in range(1, 10):
    square = value ** 2
    squares.append(square)
print(squares)

print("\n")

# In certain scenarios you would want to write cleaner and shorter code hence the above code can be simplified as below
squares = []
for value in range(1, 10):
    squares.append(value ** 2)
print(squares)

print("\n")

# The above can be further minimized using list comprehensions as shown below
squares = [value ** 2 for value in range(1, 10)] # Notice there is no colon in this case
print(squares) # prints out the same result as above

print("\n")

# Simple statistics 
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(digits))# prints out the sum of the digits in the list

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))# prints out the minimum value in the range of digits in the list

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(digits))# prints out the maximum value in the range of digits in the list