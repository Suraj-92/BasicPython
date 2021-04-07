''' 
Author: Suraj N Temkar.
Date: 07/04/2021
Title: Write a program that takes two integer command-line arguments x and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function.
'''

from math import sqrt

def Euclideandistance(x, y):
    distance = sqrt(x*x + y*y)
    print(f"Euclidean distance from the point ({x},{y}) to the origin (0, 0) = {distance}")

x = int(input("Enter the x value: "))
y = int(input("Enter the y value: "))
Euclideandistance(x, y)
