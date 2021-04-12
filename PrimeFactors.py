'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: Computes the prime factorization of N using brute force.
'''

# Function Definition
def prime_fact(x):
    try:                # Try Block
        prime_factors = []
        divisor = 2
        while divisor <= x:
            if x%divisor == 0:
                prime_factors.append(divisor)
                x = x/divisor
            else:
                divisor += 1 
        return prime_factors
    except Exception as e:         # except Block
        print("Exception is:", e)

# Main Method
if __name__ == '__main__':
    try:
        number = int(input("Enter a number to get its prime factors: "))     # User Input
        prime_fact(number)   # Function Call
        print(f"Prime Factors of {number} is : {prime_fact(number)}")

    except Exception as e:
        print("Exception occur",e)
