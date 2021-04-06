year = int(input("Enter 4-digit year: "))
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