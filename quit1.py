#!/usr/bin/python3
# Using a flag to control the user input
# This particula case we focus on the user ability to quit the program
prompt  = "Type something that will be repeated out on the screen!"
prompt += "\nType 'quit' to close the program: "

active = True  
while active == True:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)




