'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

import re

def validation():
    try:
        if re.match("^[A-Z][a-z]{2,}$", username):
            print("Username is valid",username)
            b = "Hello <<username>> How are you?"
            c = b.replace("<<username>>", username)
            print(c)
        else:
            raise Exception
    except Exception:
        print("Invalid input Please Enter The Proper Username ")

if __name__ == '__main__':
    username = input("Enter the Username: ")
    validation()

