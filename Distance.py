''' 
Author: Suraj N Temkar.
Date: 07/04/2021
Title: Write a program that takes two integer command-line arguments x and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function.
'''

from math import sqrt # Import Library

# Function Definition
def distanceFunction(x, y):
    distance = sqrt(x*x + y*y)      # Euclidean Formula
    print(f"Euclidean distance from the point (x,y) to the origin (0, 0) = {distance}")   # Print The Result

# Main Method
if __name__ == '__main__':
    try:            # Try Block
        xInput = int(input("Enter the x value: "))      # User Input X Value
        yInput = int(input("Enter the y value: "))      # User Input Y value
        distanceFunction(xInput, yInput)                # Function Call
    except Exception as e:
        print(f"Exception occur: {e} Please Enter The valid Input ")       # Exception Occur
