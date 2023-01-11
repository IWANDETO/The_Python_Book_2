#!/usr/bin/python3
#This file is used to demonstrate the use of Methods like Title in Python, alongside f-strings(Format Strings)
first_name = "IAN"
second_name = "WANDETO"
print(f"{first_name} {second_name}")

#we can assign the value of first name and second name to a single variable
full_name = f"{first_name} {second_name}"
print(full_name.title()) #.title changes only the first letter to Uppercase

print(f"Hello {full_name.title()}!")