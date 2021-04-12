''' 
Author: Suraj N Temkar.
Date: 07/04/2021
Title: A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.
'''

# Function Definition
def TwoDArray(row, column, number, double):
    arr = [[number, double]*column]*row     
    print(arr)          # Print 2D Array

# Main Method
if __name__ == '__main__':
    try:            # Try Block
        rows = int(input("Enter the number of rows: "))         # User Input
        columns = int(input("Enter the number of columns: "))   # User Input
        numbers = int(input("Enter the 1st number: "))          # User Input
        doubles = float(input("enter the 2ndt double value : ")) # User Input
        TwoDArray(rows, columns, numbers, doubles)      # Function Call
    except Exception as e:      # Exception Block
        print("Exception Occurs: ",e)       # Exception Print
