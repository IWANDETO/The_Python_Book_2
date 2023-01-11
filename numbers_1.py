#!/usr/bin/python3
#Integers can manipulated mathematically in various ways
sum = 2 + 2 # addition
2 * 2 # multiplication
10 - 5 # subtraction
8 / 4 # division
result = 2 ** 3 # exponents 

print(result)

# To follow the Bodmas, you can make use of parenthesis
result = 15 + 5 / 5
print(result)
result = (15 + 5) / 5
print(result)
#floats
result = 0.1 + 0.1
print(result)
result = 0.1 + 2
print(result)
#mixing intergers and floats will result to an output of floats

#you can use underscores with numbers to make larger numbers easier to read
num = 1_000_000_000
print(num)

#Multiple assignment, you can assign multiple values using comma provived the number of variables equals to numbers provided
x, y, z = 10, 15, 20
print(x, y, z)

#Constants
PLAYER_NUMBER = 10  
#With constants we capitalise variable names to Uppercase to show that it is a CONSTANT
#It is generally good practice to use CAPS when naming Constants 
print(PLAYER_NUMBER)