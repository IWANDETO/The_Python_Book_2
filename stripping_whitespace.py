#!/usr/bin/python3
#Python provides a function to strip whitespaces when needed to be removed
fav_language = "Python "
#There is a space after n which Python considers relevant 
print(fav_language.rstrip())

fav_framework = " Django"
print(fav_framework)
#There will be a whitespace before Django which Python won't remove until you tell it to as shown below
fav_framework = fav_framework.lstrip()
print(fav_framework)
#Reassigning the value after stripping will ensure that the whitespace is removed permanently

lang_framework = " Python Django "
print(lang_framework)
lang_framework = lang_framework.strip()
print(lang_framework)
#The strip function can be used to deal with trailing whitespaces regardless of the side entailed.