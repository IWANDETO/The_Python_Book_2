#!/usr/bin/python3
# This file demonstrates the use of break statements in Python
prompt = "Enter a Team that you would like to play for Mate!"
prompt += "\nEnter 'quit' to exit the program: "
 
while True:
    message = input(prompt)

    if message == 'quit':
        break # The break statement breaks out of the loop without executing the code after it
    else:
        print(message)