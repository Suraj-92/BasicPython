''' 
Author: Suraj N Temkar.
Date: 07/04/2021
Title: A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.
'''

# Function Definition
def sumOfThree(arr):
    a = len(arr)  # Array Length
    for i in range(0, a):
        firstnumber = arr[i]
        for j in range(i+1, a):
            secondnumber = arr[j]
            for k in range(j+1):
                thirdnumber = arr[k]

                sum = firstnumber + secondnumber + thirdnumber
                if(sum == 0):
                    print(f"{firstnumber}, {secondnumber}, {thirdnumber}")

# Main Function
if __name__ == '__main__':
    arr1 = [3, -1, -7, -4, -5, 9, -4]  # Input
    function = sumOfThree(arr1)
    print(function)     # Function Call
