''' 
Author: Suraj N Temkar.
Date: 07/04/2021
Title: A program to find the roots of the equation a*x*x + b*x + c. Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation can be found using a formula (Note: Take a, b and c as input values)
'''

from math import sqrt

def Quadratic(a, b, c):
    delta = (b*b - 4*a*c)
    sqaureroot = sqrt(delta)
    root1 = (-b - (sqaureroot))/(2*a)
    print(f"root1 of x : {root1}")

    root2 = (-b + (sqaureroot))/(2*a)
    print(f"root2 of x : {root2}")

a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))
c = int(input("Enter the c value: "))
Quadratic(a,b,c)
