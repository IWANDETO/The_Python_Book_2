#!/usr/bin/python3
#lists in python are respresented with square brackets
big_six = ['arsenal', 'manchester city', 'manchester united','chelsea','tottenham','liverpool']
print(big_six)# this will print the entire list with square brackets

# Individual items on the list are counted from 0 and not 1
print(big_six[0])

# We can also access the last item on the list using -1
print(big_six[-1])

league_leader= f"As of January 2023, the current League Leaders are {big_six[0].title()}"
print(league_leader)