''' 
Author: Suraj N Temkar.
Date: 07/04/2021
Title: A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.
'''

def Array(a, b): 
    arr = [[number, double]*column]*row
    print(arr)

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

number = int(input("Enter the Integer value : "))
double = float(input("Enter the double value : "))

Array(row, column) # Function Call

