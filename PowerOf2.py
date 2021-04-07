'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: This program takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N. 
'''

import math

def power():
    try:
        powerOf2 = math.pow(2, number)
        print(powerOf2)
    except Exception as e:
        print(f"Exception Occurs.....{e} Please Enter the proper Input")

if __name__ == '__main__':
    try:
        number = int(input("Enter a number to print power of 2 till Nth terms: "))
    except Exception as e:
        print(f"Exception Occurs.....{e} Please enter the Integer")
    power()
