''' 
Author: Suraj N Temkar.
Date: 07/04/2021
Title: A program to find the roots of the equation a*x*x + b*x + c. Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation can be found using a formula (Note: Take a, b and c as input values)
'''

from math import sqrt  # Import Library

# Function Definition
def result(a, b, c):
    delta = (b*b - 4*a*c)
    sqaureroot = sqrt(delta)
    root1 = (-b - (sqaureroot))/(2*a)
    print(f"root1 of x : {root1}")

    root2 = (-b + (sqaureroot))/(2*a)
    print(f"root2 of x : {root2}")

# Main Method
if __name__ == '__main__':
    try:            # Try Block
        input1 = int(input("Enter the a value: "))      # User Input 
        input2 = int(input("Enter the b value: "))      # User Input
        input3 = int(input("Enter the c value: "))      # User Input
        result(input1, input2, input3)      # Function Call
    except Exception as e:      # Exception Block
        print(f"Exception Occurs: {e} Please Enter the valid Input!!!!!")   # Exception Occurs
