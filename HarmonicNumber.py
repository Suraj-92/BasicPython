'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N . 
'''

# Function Definition
def harmonic():
    try:
        number = int(input("Enter the number : "))   # User Input
        harmonicNumber = 0
        for i in range(1, number+1):
            harmonicNumber += 1/i
        print(f"{number}th harmonic value is : {harmonicNumber}")
    except Exception as e:
        print(f"Exception occurs: {e} Please Enter the Integer value")

# Main Method
if __name__ == '__main__':
    harmonic()  # Function Call
