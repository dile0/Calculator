#!/usr/bin/env python3

# REWORK THIS TO SEND BACK INFORMATION TO THE MAIN.PY FILE

import math

def hyperCompPrompt():
    user_comp = 0
    print("Select a computation\n")

    while user_comp < 1 or user_comp > 7:

        print("Type 1: Hyperbolic Cosine")
        print("Type 2: Hyperbolic Sine")
        print("Type 3: Hyperbolic Tangent")
        print("Type 4: Hyperbolic Arc Cosine")
        print("Type 5: Hyperbolic Arc Sine")
        print("Type 6: Hyperbolic Arc Tangent")
        print("Type 7: Exit Program")

        user_comp = int(input("Please enter a type number: "))

        if user_comp < 1 or user_comp > 7:
            print("Invalid choice. Please try again.\n")
            print("\n")

        return user_comp

def hypCosFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        hcosChoice = input("Do you want to use the previous value? Y or N\n")
        if hcosChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue
        hyperValue = math.cosh(initialNumber)

        print("The hyperbolic value of ", initialNumber, " is ", hyperValue, ".\n")

        optionalValue = hyperValue
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return hyperValue

def hypSinFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        hsinChoice = input("Do you want to use the previous value? Y or N\n")
        if hsinChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue
        hyperValue = math.sinh(initialNumber)

        print("The hyperbolic value of ", initialNumber, " is ", hyperValue, ".\n")

        optionalValue = hyperValue
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return hyperValue

def hypTanFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        htanChoice = input("Do you want to use the previous value? Y or N\n")
        if htanChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue
        hyperValue = math.tanh(initialNumber)

        print("The hyperbolic value of ", initialNumber, " is ", hyperValue, ".\n")

        optionalValue = hyperValue
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return hyperValue

def hypAcosFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        hacosChoice = input("Do you want to use the previous value? Y or N\n")
        if hacosChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue
        hyperValue = math.acosh(initialNumber)

        print("The hyperbolic value of ", initialNumber, " is ", hyperValue, ".\n")

        optionalValue = hyperValue
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return hyperValue

def hypAsinFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        hasinChoice = input("Do you want to use the previous value? Y or N\n")
        if hasinChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue
        hyperValue = math.asinh(initialNumber)

        print("The hyperbolic value of ", initialNumber, " is ", hyperValue, ".\n")

        optionalValue = hyperValue
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return hyperValue

def hypAtanFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        hatanChoice = input("Do you want to use the previous value? Y or N\n")
        if hatanChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue
        hyperValue = math.atanh(initialNumber)

        print("The hyperbolic value of ", initialNumber, " is ", hyperValue, ".\n")

        optionalValue = hyperValue
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return hyperValue

if __name__ == "__main__":
    passAroundVal = 0.0
    while True:
        user_choice = int(hyperCompPrompt())
        match user_choice:
            case 1:
                passAroundVal = hypCosFunc(passAroundVal)
            case 2:
                passAroundVal = hypSinFunc(passAroundVal)
            case 3:
                passAroundVal = hypTanFunc(passAroundVal)
            case 4:
                passAroundVal = hypAcosFunc(passAroundVal)
            case 5:
                passAroundVal = hypAsinFunc(passAroundVal)
            case 6:
                passAroundVal = hypAtanFunc(passAroundVal)
            case 7:
                exit()