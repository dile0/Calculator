#!/usr/bin/env python3

# REWORK THIS TO SEND BACK INFORMATION TO THE MAIN.PY FILE

import math

def loopCompPrompt():
    user_comp = 0
    print("Select a computation\n")

    while user_comp < 1 or user_comp > 5:

        print("Type 1: Factorials")
        print("Type 2: Absolute Values")
        print("Type 3: Permutations")
        print("Type 4: Combinations")
        print("Type 5: Exit Program")

        print("\n")

        user_comp = int(input("Please enter a type number: "))

        if user_comp < 1 or user_comp > 5:
            print("Invalid choice. Please try again.\n")
            print("\n")

    return user_comp

def factFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        factChoice = input("Do you want to use the previous value? Y or N\n")
        if factChoice == "N":
            initialNumber = int(input("Please enter an integer for the factorial: "))
        else:
            initialNumber = int(optionalValue)
        factValue = math.factorial(initialNumber)

        print("The factorial of ", initialNumber, " is ", factValue, ".\n")

        optionalValue = factValue
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return factValue

def absFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        absChoice = input("Do you want to use the previous value? Y or N\n")
        if absChoice == "N":
            initialNumber = float(input("Please enter a value: "))
        else:
            initialNumber = optionalValue
        absValue = math.fabs(initialNumber)

        print("The absolute value of ", initialNumber, " is ", absValue, ".\n")

        optionalValue = absValue
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return absValue

def permFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        permChoice = int(input("Do you want to use the previous value as the total number [1], the number selected [2], or neither? [3]\n"))
        match permChoice:
            case 1:
                totalNumber = int(optionalValue)
                selectedNumber = int(input("Please enter an integer for the number selected: "))
            case 2:
                selectedNumber = int(optionalValue)
                totalNumber = int(input("Please enter an integer for the total number: "))
            case 3:
                selectedNumber = int(input("Please enter an integer for the number selected: "))
                totalNumber = int(input("Please enter an integer for the total number: "))
        permVal = math.perm(totalNumber, selectedNumber)

        print("The permutation of ", totalNumber, " with ", selectedNumber, " selected is ", permVal, ".\n")

        optionalValue = permVal
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return permVal

def combFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
        combChoice = int(input("Do you want to use the previous value as the total number [1], the number selected [2], or neither? [3]\n"))
        match combChoice:
            case 1:
                totalNumber = int(optionalValue)
                selectedNumber = int(input("Please enter an integer for the number selected: "))
            case 2:
                selectedNumber = int(optionalValue)
                totalNumber = int(input("Please enter an integer for the total number: "))
            case 3:
                selectedNumber = int(input("Please enter an integer for the number selected: "))
                totalNumber = int(input("Please enter an integer for the total number: "))
        combVal = math.comb(totalNumber, selectedNumber)

        print("The combination of ", totalNumber, " with ", selectedNumber, " selected is ", combVal, ".\n")

        optionalValue = combVal
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return combVal

if __name__ == "__main__":
    passAroundVal = 0.0
    while True:
        user_choice = int(loopCompPrompt())
        match user_choice:
            case 1:
                passAroundVal = factFunc(passAroundVal)
            case 2:
                passAroundVal = absFunc(passAroundVal)
            case 3:
                passAroundVal = permFunc(passAroundVal)
            case 4:
                passAroundVal = combFunc(passAroundVal)
            case 5:
                exit()

