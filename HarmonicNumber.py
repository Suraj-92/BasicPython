'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N . 
'''

number = int(input("Enter the number : "))
harmonic = 0
for i in range(1, number+1):
    harmonic += 1/i
print(f"{number}th harmonic value is : {harmonic}")
