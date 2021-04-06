def prime_fact(x):
    prime_factors = []
    divisor = 2
    while divisor <= x:
        if x%divisor == 0:
            prime_factors.append(divisor)
            x = x/divisor
        else:
            divisor += 1 
    return prime_factors

number = int(input("Enter a number to get its prime factors: "))
a = prime_fact(number)
print(f"Prime Factors of {number} is : {a}")
