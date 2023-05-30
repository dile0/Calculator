#!/usr/bin/env python3

# REWORK THIS TO SEND BACK INFORMATION TO THE MAIN.PY FILE

import math

def logCompPrompt():
    user_comp = 0
    print("Select a computation\n")

    while user_comp < 1 or user_comp > 5:

        print("Type 1: Natural Log (Base e)")
        print("Type 2: Log Base 2")
        print("Type 3: Log Base 10")
        print("Type 4: Custom Log Base")
        print("Type 5: Exit Program")


        print("\n")

        user_comp = int(input("Please enter a type number: "))

        if user_comp < 1 or user_comp > 5:
            print("Invalid choice. Please try again.\n")
            print("\n")

    return user_comp

def natLogFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        natChoice = input("Do you want to use the previous value for the argument number? Y or N\n")
        if natChoice == "N":
            argValue = float(input("Please enter a value for the argument number: "))
        else:
            argValue = optionalValue
        natLog = math.log1p(argValue)

        print("The natural log of ", argValue, " is ", natLog, ".\n")

        optionalValue = natLog
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return natLog

def base2Func(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        base2Choice = input("Do you want to use the previous value for the argument number? Y or N\n")
        if base2Choice == "N":
            argValue = float(input("Please enter a value for the argument number: "))
        else:
            argValue = optionalValue
        base2Log = math.log2(argValue)

        print("The base-2 log of ", argValue, " is ", base2Log, ".\n")

        optionalValue = base2Log
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return base2Log

def base10Func(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        base10Choice = input("Do you want to use the previous value for the argument number?? Y or N\n")
        if base10Choice == "N":
            argValue = float(input("Please enter a value for the argument number: "))
        else:
            argValue = optionalValue
        base10Log = math.log10(argValue)

        print("The base-10 log of ", argValue, " is ", base10Log, ".\n")

        optionalValue = base10Log
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return base10Log

def customLogFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        customBaseChoice = int(input("Do you want to use the previous value for the argument number [1], base number [2], or neither? [3]"))
        match customBaseChoice:
            case 1:
                argNumber = optionalValue
                baseNumber = float(input("Please enter a value for the base number: "))
            case 2:
                baseNumber = optionalValue
                argNumber = float(input("Please enter a value for the argument number: "))
            case 3:
                baseNumber = float(input("Please enter a value for the base number: "))
                argNumber = float(input("Please enter a value for the argument number: "))
        customBaseLog = math.log(argNumber,baseNumber)

        print("The base-", baseNumber, " log of ", argNumber, " is ", customBaseLog, ".\n")

        optionalValue = customBaseLog
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return customBaseLog

if __name__ == "__main__":
    passAroundVal = 0.0
    while True:
        user_choice =int(logCompPrompt())
        match user_choice:
            case 1:
                passAroundVal = natLogFunc(passAroundVal)
            case 2:
                passAroundVal = base2Func(passAroundVal)
            case 3:
                passAroundVal = base10Func(passAroundVal)
            case 4:
                passAroundVal = customLogFunc(passAroundVal)
            case 5:
                exit()