'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: This program takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N. 
'''

import math  # import Math Library 

# Function Definition
def power(number):
    try:                        # Try Block
        powerOf2 = math.pow(2, number)
        print(powerOf2)
    except Exception as e:      # Except Block
        print(f"Exception Occurs.....{e} Please Enter the proper Input")

# Main Method
if __name__ == '__main__':
    try:
        number1 = int(input("Enter a number to print power of 2 till Nth terms: "))   # User Input
        power(number1)         # Function Call
    except Exception as e:
        print(f"Exception Occurs.....{e} Please enter the Integer")
    
