''' 
Author: Suraj N Temkar.
Date: 07/04/2021
Title: A program that takes two double command-line arguments t and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the National Weather Service defines the effective temperature (the wind chill) to be:
'''


# Functio Definition
def result(temperature, speed):
    # windchill = 35.74 + (0.6215*T) + ((0.4275*T)-35.75) (V **0.16)
    windchill = 35.74 + (0.6215*temperature) - 35.75*(speed**0.16) + 0.4275*temperature*(speed**0.16)   # WindChill Formula
    print (f"wind chill temperature in Fahrenheit : {windchill}")  # Result 

# Main Method
if __name__ == '__main__':
    try:                            # Try Block
        temperature = float(input("Enter the temperature in Fahrenheit : "))  # User Input For Temperature
        print (f"......You entered {temperature} degrees. ")

        speed = float(input("Enter the wind speed : "))         # User Input For Speed
        print (f"......You entered {speed} MPH.")
        result(temperature, speed)              # Function Call
    except Exception as e:          # Exception Block
        print(f"Exception Occurs: {e} Please Enter the valid Input")
