#!/usr/bin/env python3

# REWORK THIS TO SEND BACK INFORMATION TO THE MAIN.PY FILE

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
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            adjSide = float(input("Please enter a value for the adjacent side: "))
            hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        cosSolution = float(math.cos(adjSide/hypoSide))

        print("The theta (θ) of ", adjSide, " and ", hypoSide, " is ", cosSolution, " radians.")

        optionalValue = cosSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return cosSolution

def sinFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            oppSide = float(input("Please enter a value for the opposite side: "))
            hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        sinSolution = float(math.sin(oppSide/hypoSide))

        print("The theta (θ) of ", oppSide, " and ", hypoSide, " is ", sinSolution, " radians.")

        optionalValue = sinSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return sinSolution

def tanFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            oppSide = float(input("Please enter a value for the opposite side: "))
            adjSide = float(input("Please enter a value for the adjacent side: "))
        tanSolution = float(math.tan(oppSide/adjSide))

        print("The theta (θ) of ", oppSide, " and ", adjSide, " is ", tanSolution, " radians.")

        optionalValue = tanSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return tanSolution

def secFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            adjSide = float(input("Please enter a value for the adjacent side: "))
            hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        secSolution = float(1/math.cos(adjSide/hypoSide))

        print("The theta (θ) of ", hypoSide, " and ", adjSide, " is ", secSolution, " radians.")

        optionalValue = secSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return secSolution

def cscFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            oppSide = float(input("Please enter a value for the opposite side: "))
            hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        cscSolution = float(1/math.sin(oppSide/hypoSide))

        print("The theta (θ) of ", oppSide, " and ", hypoSide, " is ", cscSolution, " radians.")

        optionalValue = cscSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return cscSolution

def cotFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            oppSide = float(input("Please enter a value for the opposite side: "))
            adjSide = float(input("Please enter a value for the adjacent side: "))
        cotSolution = float(1/math.tan(oppSide/adjSide))

        print("The theta (θ) of ", oppSide, " and ", adjSide, " is ", cotSolution, " radians.")

        optionalValue = cotSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return cotSolution

def acosFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            adjSide = float(input("Please enter a value for the adjacent side: "))
            hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        acosSolution = float(math.acos(adjSide/hypoSide))

        print("The theta (θ) of ", adjSide, " and ", hypoSide, " is ", acosSolution, " radians.")

        optionalValue = acosSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return acosSolution

def asinFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            oppSide = float(input("Please enter a value for the opposite side: "))
            hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        asinSolution = float(math.asin(oppSide/hypoSide))

        print("The theta (θ) of ", oppSide, " and ", hypoSide, " is ", asinSolution, " radians.")

        optionalValue = asinSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return asinSolution

def atanFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            oppSide = float(input("Please enter a value for the opposite side: "))
            adjSide = float(input("Please enter a value for the adjacent side: "))
        atanSolution = float(math.atan(oppSide/adjSide))

        print("The theta (θ) of ", oppSide, " and ", adjSide, " is ", atanSolution, " radians.")

        optionalValue = atanSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return atanSolution

def asecFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            adjSide = float(input("Please enter a value for the adjacent side: "))
            hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        asecSolution = float(1/math.acos(adjSide/hypoSide))

        print("The theta (θ) of ", adjSide, " and ", hypoSide, " is ", asecSolution, " radians.")

        optionalValue = asecSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return asecSolution

def acscFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            oppSide = float(input("Please enter a value for the opposite side: "))
            hypoSide = float(input("Please enter a value for the hypotenuse side: "))
        acscSolution = float(1/math.asin(oppSide/hypoSide))

        print("The theta (θ) of ", oppSide, " and ", hypoSide, " is ", acscSolution, " radians.")

        optionalValue = acscSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return acscSolution

def acotFunc(optionalValue):
    user_continue = "Y"
    while user_continue == "Y":
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
        else:
            oppSide = float(input("Please enter a value for the opposite side: "))
            adjSide = float(input("Please enter a value for the adjacent side: "))
        acotSolution = float(1/math.atan(oppSide/adjSide))

        print("The theta (θ) of ", oppSide, " and ", adjSide, " is ", acotSolution, " radians.")

        optionalValue = acotSolution

        user_continue = input("Would you like to continue? Y or N\n")
        if user_continue == "N":
            return acotSolution

if __name__ == "__main__":
    # Rework these so that the pass-in argument isn't a constant.
    passAroundVal = 0.0
    while True:
        user_choice = int(trigCompPrompt())
        match user_choice:
            case 1:
                passAroundVal = cosFunc(passAroundVal)
            case 2:
                passAroundVal = sinFunc(passAroundVal)
            case 3:
                passAroundVal = tanFunc(passAroundVal)
            case 4:
                passAroundVal = secFunc(passAroundVal)
            case 5:
                passAroundVal = cscFunc(passAroundVal)
            case 6:
                passAroundVal = cotFunc(passAroundVal)
            case 7:
                passAroundVal = acosFunc(passAroundVal)
            case 8:
                passAroundVal = asinFunc(passAroundVal)
            case 9:
                passAroundVal = atanFunc(passAroundVal)
            case 10:
                passAroundVal = asecFunc(passAroundVal)
            case 11:
                passAroundVal = acscFunc(passAroundVal)
            case 12:
                passAroundVal = acotFunc(passAroundVal)
