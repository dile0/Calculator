#!/usr/bin/env python3

# REWORK THIS TO SEND BACK INFORMATION TO THE MAIN.PY FILE

import math

def basicCompPrompt():
    user_comp = 0
    print("Select a computation\n")

    while user_comp < 1 or user_comp > 7:

        print("Type 1: Addition")
        print("Type 2: Subtraction")
        print("Type 3: Multiplication")
        print("Type 4: Division")
        print("Type 5: Square Root")
        print("Type 6: Exponential")
        print("Type 7: Exit Program\n")

        user_comp = int(input("Please enter a type number: "))

        if user_comp < 1 or user_comp > 7:
            print("Invalid choice. Please try again.\n")
            print("\n")

    return user_comp

def addition(firstNumber):
    user_continue = "Y"
    while user_continue == "Y":
        addChoice = input("Do you want to use the previous value? Y or N\n")
        if addChoice == "N":
            firstNumber = float(input("Please enter a first value: "))
        else:
            additionSum = firstNumber
        secondValue = float(input("Please enter a second value: "))
        if addChoice == "N":
            additionSum = firstNumber + secondValue
        else:
            additionSum += secondValue
        print("Your sum is: ", additionSum)

        firstNumber = additionSum
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return additionSum

def subtraction(firstNumber):
    user_continue = "Y"
    while user_continue == "Y":
        subChoice = input("Do you want to use the previous value? Y or N\n")
        if subChoice == "N":
            firstNumber = float(input("Please enter a first value: "))
        else:
            subtractionDifference = firstNumber
        secondValue = float(input("Please enter a second value: "))
        if subChoice == "N":
            subtractionDifference = firstNumber - secondValue
        else:
            subtractionDifference -= secondValue
        print("Your difference is: ", subtractionDifference)

        firstNumber = subtractionDifference
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return subtractionDifference


def multiplication(firstNumber):
    user_continue = "Y"
    while user_continue == "Y":
        multChoice = input("Do you want to use the previous value? Y or N\n")
        if multChoice == "N":
            firstNumber = float(input("Please enter a first value: "))
        else:
            multiplicationProduct = firstNumber
        secondValue = float(input("Please enter a second value: "))
        if multChoice == "N":
            multiplicationProduct = firstNumber * secondValue
        else:
            multiplicationProduct *= secondValue
        print("Your product is: ", multiplicationProduct)

        firstNumber = multiplicationProduct
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return multiplicationProduct

def division(firstNumber):
    user_continue = "Y"
    while user_continue == "Y":
        divChoice = input("Do you want to use the previous value? Y or N\n")
        if divChoice == "N":
            firstNumber = float(input("Please enter a first value: "))
        else:
            divisionQuotient = firstNumber
        secondValue = float(input("Please enter a second value:"))
        typeOfDivision = int(input("What type of division would you like to perform? 1 for Standard, 2 for Modulus\n"))
        if divChoice == "Y":
            match typeOfDivision:
                case 1:
                    divisionQuotient /= secondValue
                case 2:
                    divisionQuotient %= secondValue
                case _:
                    print("Please try again and enter either a 1 or 2\n")
        else:
            match typeOfDivision:
                case 1:
                    divisionQuotient = firstNumber / secondValue
                case 2:
                    divisionQuotient = firstNumber % secondValue
                case _:
                    print("Please try again and enter either a 1 or 2\n")

        print("Your quotient is: ", divisionQuotient)

        firstNumber = divisionQuotient
        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            divisionQuotient

def squareRoot(firstNumber):
    user_continue = "Y"
    while user_continue == "Y":
        squareChoice = input("Do you want to use the previous value? Y or N\n")
        if squareChoice == "N":
            firstNumber = float(input("Please enter the base value: "))
        squareRootNew = math.sqrt(firstNumber)
        print("The Square Root of ", firstNumber, " is ", squareRootNew)

        firstNumber = squareRootNew

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return squareRootNew

def exponentials(firstNumber):
    user_continue = "Y"
    while user_continue == "Y":
        expoChoice = input("Do you want to use the previous value? Y or N\n")
        if expoChoice == "N":
            baseNumber = float(input("Please enter a number for the base value: "))
        else:
            baseNumber = firstNumber
        exponentValue = float(input("Please enter a second value for the exponent: "))
        total = pow(baseNumber, exponentValue)
        print(baseNumber, " to the power of ", exponentValue, " is ", total)

        firstNumber = total

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return total

if __name__ == "__main__":
    passAroundVal = 0.0
    while True:
        user_choice = int(basicCompPrompt())
        match user_choice:
            case 1:
                passAroundVal = addition(passAroundVal)
            case 2:
                passAroundVal = subtraction(passAroundVal)
            case 3:
                passAroundVal = multiplication(passAroundVal)
            case 4:
                passAroundVal = division(passAroundVal)
            case 5:
                passAroundVal = squareRoot(passAroundVal)
            case 6:
                passAroundVal = exponentials(passAroundVal)
            case 7:
                exit()
    
