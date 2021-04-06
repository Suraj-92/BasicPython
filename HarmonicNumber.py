number = int(input("Enter the number : "))
harmonic = 0
for i in range(1, number+1):
    harmonic += 1/i
print(f"{number}th harmonic value is : {harmonic}")
