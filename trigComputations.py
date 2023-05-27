#!/usr/bin/env python3

# REWORK THIS TO SEND BACK INFORMATION TO THE MAIN.PY FILE
# REWORK THIS TO ALLOW VALUES TO TRANSFER FROM PROCESS TO PROCESS AND RESET VALUES

import math

def trigCompPrompt():
    user_comp = 0
    print("Select a computation\n")

    while user_comp < 1 or user_comp > 12:

        print("Type 1: Cosine")
        print("Type 2: Sine")
        print("Type 3: Tangent")
        print("Type 4: Secant")
        print("Type 5: Cosecant")
        print("Type 6: Cotangent")
        print("Type 7: Arc Cosine")
        print("Type 8: Arc Sine")
        print("Type 9: Arc Tangent")
        print("Type 10: Arc Secant")
        print("Type 11: Arc Cosecant")
        print("Type 12: Arc Cotangent")

        user_comp = int(input("Please enter a type number:"))

        if user_comp < 1 or user_comp > 12:
            print("Invalid choice. Please try again.\n")
            print("\n")

    return user_comp

def cosFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            cos_choice = int(input("Do you want the previous value to be the adjacent side [1], hypotenuse side [2], or neither? [3]"))
            match cos_choice:
                case 1:
                    adjSide = optionalValue
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
                case 2:
                    hypoSide = optionalValue
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                case _:
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        cosSolution = float(math.cos(adjSide/hypoSide))

        print("The theta (θ) of ", adjSide, " and ", hypoSide, " is ", cosSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def sinFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            sin_choice = int(input("Do you want the previous value to be the opposite side [1], hypotenuse side [2], or neither? [3]"))
            match sin_choice:
                case 1:
                    oppSide = optionalValue
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
                case 2:
                    hypoSide = optionalValue
                    oppSide = float(input("Please enter a value for the opposite side: "))
                case _:
                    oppSide = float(input("Please enter a value for the opposite side: "))
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        sinSolution = float(math.sin(oppSide/hypoSide))

        print("The theta (θ) of ", oppSide, " and ", hypoSide, " is ", sinSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def tanFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            tan_choice = int(input("Do you want the previous value to be the opposite side [1], adjacent side [2], or neither? [3]"))
            match tan_choice:
                case 1:
                    oppSide = optionalValue
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                case 2:
                    adjSide = optionalValue
                    oppSide = float(input("Please enter a value for the opposite side: "))
                case _:
                    oppSide = float(input("Please enter a value for the opposite side: "))
                    adjSide = float(input("Please enter a value for the adjacent side: "))
        tanSolution = float(math.tan(oppSide/adjSide))

        print("The theta (θ) of ", oppSide, " and ", adjSide, " is ", tanSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def secFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            sec_choice = int(input("Do you want the previous value to be the adjacent side [1], hypotenuse side [2], or neither? [3]"))
            match sec_choice:
                case 1:
                    adjSide = optionalValue
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
                case 2:
                    hypoSide = optionalValue
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                case _:
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        secSolution = float(1/math.cos(adjSide/hypoSide))

        print("The theta (θ) of ", hypoSide, " and ", adjSide, " is ", secSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def cscFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            csc_choice = int(input("Do you want the previous value to be the opposite side [1], hypotenuse side [2], or neither? [3]"))
            match csc_choice:
                case 1:
                    oppSide = optionalValue
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
                case 2:
                    hypoSide = optionalValue
                    oppSide = float(input("Please enter a value for the opposite side: "))
                case _:
                    oppSide = float(input("Please enter a value for the opposite side: "))
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        cscSolution = float(1/math.sin(oppSide/hypoSide))

        print("The theta (θ) of ", oppSide, " and ", hypoSide, " is ", cscSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def cotFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            cot_choice = int(input("Do you want the previous value to be the opposite side [1], adjacent side [2], or neither? [3]"))
            match cot_choice:
                case 1:
                    oppSide = optionalValue
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                case 2:
                    adjSide = optionalValue
                    oppSide = float(input("Please enter a value for the opposite side: "))
                case _:
                    oppSide = float(input("Please enter a value for the opposite side: "))
                    adjSide = float(input("Please enter a value for the adjacent side: "))
        cotSolution = float(1/math.tan(oppSide/adjSide))

        print("The theta (θ) of ", oppSide, " and ", adjSide, " is ", cotSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def acosFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            acos_choice = int(input("Do you want the previous value to be the adjacent side [1], hypotenuse side [2], or neither? [3]"))
            match acos_choice:
                case 1:
                    adjSide = optionalValue
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
                case 2:
                    hypoSide = optionalValue
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                case _:
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        acosSolution = float(math.acos(adjSide/hypoSide))

        print("The theta (θ) of ", adjSide, " and ", hypoSide, " is ", acosSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def asinFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            asin_choice = int(input("Do you want the previous value to be the opposite side [1], hypotenuse side [2], or neither? [3]"))
            match asin_choice:
                case 1:
                    oppSide = optionalValue
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
                case 2:
                    hypoSide = optionalValue
                    oppSide = float(input("Please enter a value for the opposite side: "))
                case _:
                    oppSide = float(input("Please enter a value for the opposite side: "))
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        asinSolution = float(math.asin(oppSide/hypoSide))

        print("The theta (θ) of ", oppSide, " and ", hypoSide, " is ", asinSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def atanFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            atan_choice = int(input("Do you want the previous value to be the opposite side [1], adjacent side [2], or neither? [3]"))
            match atan_choice:
                case 1:
                    oppSide = optionalValue
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                case 2:
                    adjSide = optionalValue
                    oppSide = float(input("Please enter a value for the opposite side: "))
                case _:
                    oppSide = float(input("Please enter a value for the opposite side: "))
                    adjSide = float(input("Please enter a value for the adjacent side: "))
        atanSolution = float(math.atan(oppSide/adjSide))

        print("The theta (θ) of ", oppSide, " and ", adjSide, " is ", atanSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def asecFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            asec_choice = int(input("Do you want the previous value to be the adjacent side [1], hypotenuse side [2], or neither? [3]"))
            match asec_choice:
                case 1:
                    adjSide = optionalValue
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
                case 2:
                    hypoSide = optionalValue
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                case _:
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        asecSolution = float(1/math.acos(adjSide/hypoSide))

        print("The theta (θ) of ", adjSide, " and ", hypoSide, " is ", asecSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def acscFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            acsc_choice = int(input("Do you want the previous value to be the opposite side [1], hypotenuse side [2], or neither? [3]"))
            match acsc_choice:
                case 1:
                    oppSide = optionalValue
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
                case 2:
                    hypoSide = optionalValue
                    oppSide = float(input("Please enter a value for the opposite side: "))
                case _:
                    oppSide = float(input("Please enter a value for the opposite side: "))
                    hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        acscSolution = float(1/math.asin(oppSide/hypoSide))

        print("The theta (θ) of ", oppSide, " and ", hypoSide, " is ", acscSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

def acotFunc(optionalValue):
    while True:
        if optionalValue != 0.0:
            acot_choice = int(input("Do you want the previous value to be the opposite side [1], adjacent side [2], or neither? [3]"))
            match acot_choice:
                case 1:
                    oppSide = optionalValue
                    adjSide = float(input("Please enter a value for the adjacent side: "))
                case 2:
                    adjSide = optionalValue
                    oppSide = float(input("Please enter a value for the opposite side: "))
                case _:
                    oppSide = float(input("Please enter a value for the opposite side: "))
                    adjSide = float(input("Please enter a value for the adjacent side: "))
        acotSolution = float(1/math.atan(oppSide/adjSide))

        print("The theta (θ) of ", oppSide, " and ", adjSide, " is ", acotSolution, " radians.")

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            break;

if __name__ == "__main__":
    # Rework these so that the pass-in argument isn't a constant.
    user_choice = int(trigCompPrompt())
    match user_choice:
        case 1:
            cosFunc(1)
        case 2:
            sinFunc(1)
        case 3:
            tanFunc(1)
        case 4:
            secFunc(1)
        case 5:
            cscFunc(1)
        case 6:
            cotFunc(1)
        case 7:
            acosFunc(1)
        case 8:
            asinFunc(1)
        case 9:
            atanFunc(1)
        case 10:
            asecFunc(1)
        case 11:
            acscFunc(1)
        case 12:
            acotFunc(1)