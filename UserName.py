'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

import re    # import Regular Expression Library

# Function
def validation(username):
    try:                                                           # Try Block
        if re.match("^[A-Z][a-z]{2,}$", username):                 # Regex Pattern
            print("Username is valid",username)
            b = "Hello <<username>> How are you?"               
            c = b.replace("<<username>>", username)                # Replace method
            print(c)
        else:
            raise Exception
    except Exception:
        print("Invalid input Please Enter The Proper Username ")
    finally:                                                        # Finally block
        print("......................")

#Main Method
if __name__ == '__main__':
    username1 = input("Enter the Username: ")  # User Input
    validation(username1)                      # Function Call
