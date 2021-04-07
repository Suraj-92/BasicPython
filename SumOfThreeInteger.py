''' 
Author: Suraj N Temkar.
Date: 07/04/2021
Title: A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.
'''

def sumOfThree(arr):
    a = len(arr)
    for i in range(0, a):
        firstnumber = arr[i]
        for j in range(i+1, a):
            secondnumber = arr[j]
            for k in range(j+1):
                thirdnumber = arr[k]

                sum = firstnumber + secondnumber + thirdnumber
                if(sum == 0):
                    print(f"{firstnumber}, {secondnumber}, {thirdnumber}")

arr = [3, -1, -7, -4, -5, 9, -4]
function = sumOfThree(arr)
print(function)
                