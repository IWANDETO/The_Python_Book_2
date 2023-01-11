#!/usr/bin/python3
# Python supports an elif statement which is an if statement that is executed when the default if statement fails the test
# Consider the below code that determines amount to pay for entering an amusement park based on age
age = 1
if age < 25:
    print("Your fee is 0 Ksh")
elif age < 18:
    print("Your fee is 100 Ksh")
else:
    print("Your fee is 250 Ksh")

# The else statement is executed when all the above conditions have not been meet
# However youd don't have to use an else statement if you have specific conditions to be meet all round
# Consider a grading system below

marks = 810
if marks < 40:
    grade = "E"
elif marks <= 50:
    grade = "D"
elif marks <= 60:
    grade = "C"
elif marks <= 70:
    grade = "B"
elif marks <= 100:
    grade = "A"
else:
    grade = "out of Range"
print(f"\nYour grade is {grade}")

age = 66
if age < 5:
    fee = "0"
elif age < 18:
    fee = "100"
elif age < 65:
    fee = "250"
elif age >= 65:
    fee = "150"
print(f"\nYour fee is Ksh {fee}.\n")

# Consider the code below for adding toppings to Pizza
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")