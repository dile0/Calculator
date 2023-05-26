#!/usr/bin/env python3

# REWORK THIS TO SEND BACK INFORMATION TO THE MAIN.PY FILE
# REWORK THIS TO ALLOW VALUES TO TRANSFER FROM PROCESS TO PROCESS AND RESET VALUES

import math

def basicCompPrompt():
    user_comp = 0
    print("Select a computation\n")

    while user_comp < 1 or user_comp > 6:

        print("Type 1: Addition")
        print("Type 2: Subtraction")
        print("Type 3: Multiplication")
        print("Type 4: Division")
        print("Type 5: Square Root")
        print("Type 6: Exponential\n")
        user_comp = int(input("Please enter a type number:"))

        if user_comp < 1 or user_comp > 6:
            print("Invalid choice. Please try again.\n")
            print("\n")

    return user_comp

def addition(firstNumber):
    additionSum = firstNumber
    while True:
        secondValue = float(input("Please enter a second value:"))
        additionSum += secondValue
        print("Your sum is: ", additionSum)
        
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def subtraction(firstNumber):
    subtractionDifference = firstNumber
    while True:
        secondValue = float(input("Please enter a second value:"))
        subtractionDifference -= secondValue
        print("Your difference is: ", subtractionDifference)
        
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;


def multiplication(firstNumber):
    multiplicationProduct = firstNumber
    while True:
        secondValue = float(input("Please enter a second value:"))
        multiplicationProduct *= secondValue
        print("Your product is: ", multiplicationProduct)
        
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def division(firstNumber):
    divisionQuotient = firstNumber
    while True:
        secondValue = float(input("Please enter a second value:"))
        typeOfDivision = int(input("What type of division would you like to perform? 1 for Standard, 2 for Modulus\n"))
        match typeOfDivision:
            case 1:
                divisionQuotient /= secondValue
            case 2:
                divisionQuotient %= secondValue
            case _:
                print("Please try again and enter either a 1 or 2\n")
        print("Your quotient is: ", divisionQuotient)

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def squareRoot(firstNumber):
    squareRootOrig = firstNumber
    while True:
        squareRootNew = math.sqrt(squareRootOrig)
        print("The Square Root of ", squareRootOrig, " is ", squareRootNew)

        squareRootOrig = squareRootNew

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def exponentials(firstNumber):
    baseNumber = firstNumber
    while True:
        exponentValue = float(input("Please enter a second value for the exponent"))
        total = pow(baseNumber, exponentValue)
        print(baseNumber, " to the power of ", exponentValue, " is ", total)

        baseNumber = total

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

if __name__ == "__main__":
    firstValue = input("Enter your first value:")
    firstValue = float(firstValue)
    user_choice = basicCompPrompt()
    user_choice = int(user_choice)
    match user_choice:
        case 1: 
            addition(firstValue)
        case 2:
            subtraction(firstValue)
        case 3:
            multiplication(firstValue)
        case 4:
            division(firstValue)
        case 5:
            squareRoot(firstValue)
        case 6:
            exponentials(firstValue)
        
    
