''' 
Author: Suraj N Temkar.
Date: 07/04/2021
Title: A program that takes two double command-line arguments t and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the National Weather Service defines the effective temperature (the wind chill) to be:
'''

def windChill():
    temperature = float(input("Enter the temperature in Fahrenheit : "))
    print (f"......You entered {temperature} degrees : ")

    speed = float(input("Enter the wind speed : "))
    print (f"......You entered {speed} MPH.")
    # windchill = 35.74 + (0.6215*T) + ((0.4275*T)-35.75) (V **0.16)
    windchill = 35.74 + (0.6215*temperature) - 35.75*(speed**0.16) + 0.4275*temperature*(speed**0.16)

    print (f"Wind chill temperature in Fahrenheit : {windchill}")

windChill()