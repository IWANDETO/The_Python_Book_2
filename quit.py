#!/usr/bin/python3
""" This Program takes input from the User and the user also decides when to quit
The program simulates a parrot which repeats words back to a person
But this case has a quit option"""
prompt = "Enter a Message that will be repeated out on the screen: "
prompt += "\nYou can type 'quit' to exit the program! "

"""message = "" # We assign an empty string to message to enable Python to do a comparison
while message != "quit":
    message = input(prompt)
    print(message)"""

# The above code prints out 'quit' before closing the program, we can use if statement to take care of that

message = "" # We assign an empty string to message to enable Python to do a comparison
while message != "quit":
    message = input(prompt)

    if message != 'quit':
        print(message)