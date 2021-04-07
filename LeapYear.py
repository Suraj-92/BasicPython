'''
Author: Suraj N Temkar.
Date: 05/04/2021
Title: Check year is Leap Year or Not.
'''

def leapYear():
    try:
        isLeap = False
        if(year%4 == 0):
            if(year% 100 == 0):
                if(year%400 == 0):
                    isLeap = True
                else:
                    isLeap = False
            else:
                isLeap = True
        else:
            isLeap = False

        if(isLeap == True):
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
    except Exception as e:
        print("Exception is: ", e)

if __name__ == '__main__':
    try:
        year = int(input("Enter 4-digit year: "))
    except Exception as e:
        print(f"Exception occurs.....{e}.....Please enter 4-Digit Number")
    leapYear()
