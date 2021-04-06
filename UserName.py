'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

import re
username = input("Enter the Username: ")

if re.match("^[A-Z][a-z]{2,}$", username):
    print("Username is valid")
    b = "Hello <<username>> How are you?"
    c = b.replace("<<username>>", username)
    print(c)
else:
    print("Invalid Username")

print("Done")
