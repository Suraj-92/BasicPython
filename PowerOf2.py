'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: This program takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N. 
'''

import math
number = int(input("Enter a number to print power of 2 till Nth terms: "))
a = math.pow(2, number)
print(a)