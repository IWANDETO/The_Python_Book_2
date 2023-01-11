#!/usr/bin/python3
# Program takes a poll from players who key in the user input
responses = {}
active = True # Set the flag to active

while active:
    name = input("Enter your name: ")
    team = input("Which team would like to play for: ")

    responses[name] = team

    repeat = input("\nWould you like to let someone else do the poll? (yes/no) : ")
    if repeat == 'no':
        active = False
    
print("\nPoll results are as follows: \n")
for name, team in responses.items():
    print(f"{name.title()} would like to play for {team}!")


