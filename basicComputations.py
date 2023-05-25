#!/usr/bin/env python3

import os
import sys
import argparse

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
        
        user_continue = input("Y or N\n")
        if user_continue == "N":
            break;

def subtraction(firstNumber):
    subtractionDifference = firstNumber
    while True:
        secondValue = float(input("Please enter a second value:"))
        subtractionDifference -= secondValue
        print("Your difference is: ", subtractionDifference)
        
        user_continue = input("Y or N\n")
        if user_continue == "N":
            break;


def multiplication(firstNumber):
    multiplicationProduct = firstNumber
    while True:
        secondValue = float(input("Please enter a second value:"))
        multiplicationProduct *= secondValue
        print("Your product is: ", multiplicationProduct)
        
        user_continue = input("Y or N\n")
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
        
    
