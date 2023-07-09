#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess

# Import the commputation modules
import basicComputations
import trigComputations
import logComputations
import loopComputations
import hyperComputations
import unitConversions

def startUpPrompt():

    user_type = 0
    print("Welcome to the Fundamental Calculator!\n")
    print("\n")    
    #Insert some fun text art for a calcuator here
    print("What type of computation would you like to perform?\n")

    while user_type < 1 or user_type > 7:

        print("Type 1: Basic Computation")
        print("Type 2: Trigonometric Functions")
        print("Type 3: Logarithmic Functions")
        print("Type 4: Factorials, Absolutes, Permutations & Combinations")
        print("Type 5: Hyperbolic Functions")
        print("Type 6: Unit Conversions")
        print("Type 7: Exit System\n")
        user_type = int(input("Please enter a type number:"))
        
        if user_type < 1 or user_type > 7:
            print("Invalid choice. Please try again.\n")
            print("\n")

    return  user_type

if __name__ == "__main__":
    while True:
        user_choice = startUpPrompt()
        print("You chose type: ", user_choice)
        match user_choice:
            case 1:
                subprocess.run(["python", "basicComputations.py"])
            case 2:
                subprocess.run(["python", "trigComputations.py"])
            case 3:
                subprocess.run(["python", "logComputations.py"])
            case 4:
                subprocess.run(["python", "loopComputations.py"])
            case 5:
                subprocess.run(["python", "hyperComputations.py"])
            case 6:
                subprocess.run(["python", "unitConversions.py"])
            case 7:
                exit()