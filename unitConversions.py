#!/usr/bin/env python3

# REWORK THIS TO SEND BACK INFORMATION TO THE MAIN.PY FILE

import math

def unitConvPrompt():
    user_comp = 0
    print("Select a conversion\n")

    while user_comp < 1 or user_comp > 7:

        print("Type 1: Length")
        print("Type 2: Weight")
        print("Type 3: Temperature")
        print("Type 4: Volume")
        print("Type 5: Time")
        print("Type 6: Speed")
        print("Type 7: Exit Program")

        user_comp = int(input("Please enter a type number: "))

        if user_comp < 1 or user_comp > 7:
            print("Invalid choice. Please try again.\n")
            print("\n")

        return user_comp

def lengthConv(optionalValue):
    user_continue ="Y"
    while user_continue == "Y":

        lengthChoice = input("Do you want to use the previous value? Y or N\n")
        if lengthChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue

        conversionType = 0
        while conversionType < 1 or conversionType > 6:

            print("Select a length-based conversion\n")

            print("Type 1: Inches to Centimeters")
            print("Type 2: Centimeters to Inches")
            print("Type 3: Feet to Meters")
            print("Type 4: Meters to Feet")
            print("Type 5: Miles to Kilometers")
            print("Type 6: Kilometers to Miles")

            conversionType = int(input("Please enter a type number: "))

            if conversionType < 1 or conversionType > 6:
                print("Invalid choice. Please try again.\n")
                print("\n")

        match conversionType:
            case 1:
                convertedNumber = initialNumber * 2.54
                print(initialNumber, " inches is equivalent to ", convertedNumber, " centimeters.\n")
            case 2:
                convertedNumber = initialNumber / 2.54
                print(initialNumber, " centimeters is equivalent to ", convertedNumber, " inches.\n")
            case 3:
                convertedNumber = initialNumber / 3.281
                print(initialNumber, " feet is equivalent to ", convertedNumber, " meters.\n")
            case 4:
                convertedNumber = initialNumber * 3.281
                print(initialNumber, " meters is equivalent to ", convertedNumber, " feet.\n")
            case 5:
                convertedNumber = initialNumber * 1.609
                print(initialNumber, " miles is equivalent to ", convertedNumber, " kilometers.\n")
            case 6:
                convertedNumber = initialNumber / 1.609
                print(initialNumber, " kilometers is equivalent to ", convertedNumber, " miles.\n")

        optionalValue = convertedNumber
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return convertedNumber

def weightConv(optionalValue):
    user_continue ="Y"
    while user_continue == "Y":

        weightChoice = input("Do you want to use the previous value? Y or N\n")
        if weightChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue

        conversionType = 0
        while conversionType < 1 or conversionType > 4:

            print("Select a weight-based conversion\n")

            print("Type 1: Ounces to Grams")
            print("Type 2: Grams to Ounces")
            print("Type 3: Pounds to Kilograms")
            print("Type 4: Kilograms to Pounds")

            conversionType = int(input("Please enter a type number: "))

            if conversionType < 1 or conversionType > 4:
                print("Invalid choice. Please try again.\n")
                print("\n")

        match conversionType:
            case 1:
                convertedNumber = initialNumber * 28.35
                print(initialNumber, " ounces is equivalent to ", convertedNumber, " grams.\n")
            case 2:
                convertedNumber = initialNumber / 28.35
                print(initialNumber, " grams is equivalent to ", convertedNumber, " ounces.\n")
            case 3:
                convertedNumber = initialNumber / 2.205
                print(initialNumber, " pounds is equivalent to ", convertedNumber, " kilograms.\n")
            case 4:
                convertedNumber = initialNumber * 2.205
                print(initialNumber, " kilograms is equivalent to ", convertedNumber, " pounds.\n")

        optionalValue = convertedNumber
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return convertedNumber

def tempConv(optionalValue):
    user_continue ="Y"
    while user_continue == "Y":

        tempChoice = input("Do you want to use the previous value? Y or N\n")
        if tempChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue

        conversionType = 0
        while conversionType < 1 or conversionType > 6:

            print("Select a temperature-based conversion\n")

            print("Type 1: Celsius to Fahrenheit")
            print("Type 2: Fahrenheit to Celsius")
            print("Type 3: Celsius to Kelvin")
            print("Type 4: Kelvin to Celsius")
            print("Type 5: Fahrenheit to Kelvin")
            print("Type 6: Kelvin to Fahrenheit")

            conversionType = int(input("Please enter a type number: "))

            if conversionType < 1 or conversionType > 6:
                print("Invalid choice. Please try again.\n")
                print("\n")

        match conversionType:
            case 1:
                convertedNumber = (initialNumber * 9/5) + 32
                print(initialNumber, " degrees celsius is equivalent to ", convertedNumber, " degrees fahrenheit.\n")
            case 2:
                convertedNumber = (initialNumber - 32) * 5/9
                print(initialNumber, " degrees fahrenheit is equivalent to ", convertedNumber, " degrees celsius.\n")
            case 3:
                convertedNumber = initialNumber + 273.15
                print(initialNumber, " degrees celsius is equivalent to ", convertedNumber, " degrees kelvin.\n")
            case 4:
                convertedNumber = initialNumber - 273.15
                print(initialNumber, " degrees kelvin is equivalent to ", convertedNumber, " degrees celsius.\n")
            case 5:
                convertedNumber = (((initialNumber - 32) * 5/9) + 273.15)
                print(initialNumber, " degrees fahrenheit is equivalent to ", convertedNumber, " degrees kelvin.\n")
            case 6:
                convertedNumber = (((initialNumber - 273.15) * 9/5) + 32)
                print(initialNumber, " degrees kelvin is equivalent to ", convertedNumber, " degrees fahrenheit.\n")

        optionalValue = convertedNumber
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return convertedNumber

def volConv(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":

        volumeChoice = input("Do you want to use the previous value? Y or N\n")
        if volumeChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue

        conversionType = 0
        while conversionType < 1 or conversionType > 8:

            print("Select a volume-based conversion type\n")

            print("Type 1: Cubic Centimeters to Liters")
            print("Type 2: Liters to Cubic Centimeters")
            print("Type 3: Cubic Meters to Liters")
            print("Type 4: Liters to Cubic Meters")
            print("Type 5: Milliliters to Liters")
            print("Type 6: Liters to Milliliters")
            print("Type 7: Gallons to Liters")
            print("Type 8: Liters to Gallons")

            conversionType = int(input("Please enter a type number: "))

            if conversionType < 1 or conversionType > 8:
                print("Invalid choice. Please try again.\n")
                print("\n")

        match conversionType:
            case 1:
                convertedNumber = initialNumber / 1000
                print(initialNumber, " cubic centimeters is equivalent to ", convertedNumber, " liters.\n")
            case 2:
                convertedNumber = initialNumber * 1000
                print(initialNumber, " liters is equivalent to ", convertedNumber, " cubic centimeters.\n")
            case 3:
                convertedNumber = initialNumber * 1000
                print(initialNumber, " cubic meters is equivalent to ", convertedNumber, " liters.\n")
            case 4:
                convertedNumber = initialNumber / 1000
                print(initialNumber, " liters is equivalent to ", convertedNumber, " cubic meters.\n")
            case 5:
                convertedNumber = initialNumber / 1000
                print(initialNumber, " milliliters is equivalent to ", convertedNumber, " liters.\n")
            case 6:
                convertedNumber = initialNumber * 1000
                print(initialNumber, " liters is equivalent to ", convertedNumber, " milliliters.\n")
            case 7:
                convertedNumber = initialNumber * 3.78541
                print(initialNumber, " gallons is equivalent to ", convertedNumber, " liters.\n")
            case 8:
                convertedNumber = initialNumber * 0.264172
                print(initialNumber, " liters is equivalent to ", convertedNumber, " gallons.\n")

        optionalValue = convertedNumber
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return convertedNumber

def timeConv(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":

        timeChoice = input("Do you want to use the previous value? Y or N\n")
        if timeChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue

        conversionType = 0
        while conversionType < 1 or conversionType > 10:

            print("Select a time-based conversion type\n")

            print("Type 1: Seconds to Minutes")
            print("Type 2: Minutes to Hours")
            print("Type 3: Hours to Days")
            print("Type 4: Days to Weeks")
            print("Type 5: Weeks to Months")
            print("Type 6: Months to Years")
            print("Type 7: Hours to Minutes")
            print("Type 8: Days to Hours")
            print("Type 9: Years to Seconds")
            print("Type 10: Minutes to Seconds")

            conversionType = int(input("Please enter a type number: "))

            if conversionType < 1 or conversionType > 10:
                print("Invalid choice. Please try again.\n")
                print("\n")

        match conversionType:
            case 1:
                convertedNumber = initialNumber / 60
                print(initialNumber, " seconds is equivalent to ", convertedNumber, " minutes.\n")
            case 2:
                convertedNumber = initialNumber / 60
                print(initialNumber, " minutes is equivalent to ", convertedNumber, " hours.\n")
            case 3:
                convertedNumber = initialNumber / 24
                print(initialNumber, " hours is equivalent to ", convertedNumber, " days.\n")
            case 4:
                convertedNumber = initialNumber / 7
                print(initialNumber, " days is equivalent to ", convertedNumber, " weeks.\n")
            case 5:
                convertedNumber = initialNumber / 4.345
                print(initialNumber, " weeks is equivalent to ", convertedNumber, " months.\n")
            case 6:
                convertedNumber = initialNumber / 12
                print(initialNumber, " months is equivalent to ", convertedNumber, " years.\n")
            case 7:
                convertedNumber = initialNumber * 60
                print(initialNumber, " hours is equivalent to ", convertedNumber, " minutes.\n")
            case 8:
                convertedNumber = initialNumber * 24
                print(initialNumber, " days is equivalent to ", convertedNumber, " hours.\n")
            case 9:
                convertedNumber = initialNumber * 31536000
                print(initialNumber, " years is equivalent to ", convertedNumber, " seconds.\n")
            case 10:
                convertedNumber = initialNumber * 60
                print(initialNumber, " minutes is equivalent to ", convertedNumber, " seconds.\n")

        optionalValue = convertedNumber
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return convertedNumber

def speedConv(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":

        speedChoice = input("Do you want to use the previous value? Y or N\n")
        if speedChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue

        conversionType = 0
        while conversionType < 1 or conversionType > 10:

            print("Select a speed-based conversion type\n")

            print("Type 1: Meters/Second to Kilometers/Hour")
            print("Type 2: Kilometers/Hour to Meters/Second")
            print("Type 3: Miles/Hour to Kilometers/Hour")
            print("Type 4: Kilometers/Hour to Miles/Hour")
            print("Type 5: Knots to Kilometers/Hour")
            print("Type 6: Kilometers/Hour to Knots")
            print("Type 7: Feet/Second to Meters/Second")
            print("Type 8: Meters/Second to Feet/Second")
            print("Type 9: Mach to Meters/Second")
            print("Type 10: Meters/Second to Mach")

            conversionType = int(input("Please enter a type number: "))

            if conversionType < 1 or conversionType > 10:
                print("Invalid choice. Please try again.\n")
                print("\n")

        match conversionType:
            case 1:
                convertedNumber = initialNumber * 3.6
                print(initialNumber, " m/s is equivalent to ", convertedNumber, " km/h.\n")
            case 2:
                convertedNumber = initialNumber / 3.6
                print(initialNumber, " km/h is equivalent to ", convertedNumber, " m/s.\n")
            case 3:
                convertedNumber = initialNumber * 1.60934
                print(initialNumber, " mph is equivalent to ", convertedNumber, " km/h.\n")
            case 4:
                convertedNumber = initialNumber / 1.60934
                print(initialNumber, " km/h is equivalent to ", convertedNumber, " mph.\n")
            case 5:
                convertedNumber = initialNumber * 1.852
                print(initialNumber, " knots is equivalent to ", convertedNumber, " km/h.\n")
            case 6:
                convertedNumber = initialNumber / 1.852
                print(initialNumber, " km/h is equivalent to ", convertedNumber, " knots.\n")
            case 7:
                convertedNumber = initialNumber * 0.3048
                print(initialNumber, " ft/s is equivalent to ", convertedNumber, " m/s.\n")
            case 8:
                convertedNumber = initialNumber / 0.3048
                print(initialNumber, " m/s is equivalent to ", convertedNumber, " ft/s.\n")
            case 9:
                convertedNumber = initialNumber * 343
                print(initialNumber, " mach is equivalent to ", convertedNumber, " m/s.\n")
            case 10:
                convertedNumber = initialNumber / 343
                print(initialNumber, " m/s is equivalent to ", convertedNumber, " mach.\n")

        optionalValue = convertedNumber
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return convertedNumber

if __name__ == "__main__":
    passAroundVal = 0.0
    while True:
        user_choice = int(unitConvPrompt())
        match user_choice:
            case 1:
                passAroundVal = lengthConv(passAroundVal)
            case 2:
                passAroundVal = weightConv(passAroundVal)
            case 3:
                passAroundVal = tempConv(passAroundVal)
            case 4:
                passAroundVal = volConv(passAroundVal)
            case 5:
                passAroundVal = timeConv(passAroundVal)
            case 6:
                passAroundVal = speedConv(passAroundVal)
            case 7:
                exit()