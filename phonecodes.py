#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getPhoneNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def getPhoneNumber(s):
    
    word_to_digit ={
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    converted = ""
    multiplier_stack = []
    for token in s.split():
        if token == "double":
            multiplier_stack.append(2)
        elif token == "triple":
            multiplier_stack.append(3)
        else:
            mutliplier = multiplier_stack.pop() if multiplier_stack else 1
            converted += word_to_digit[token] * mutliplier
            
    return converted

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getPhoneNumber(s)

    fptr.write(result + '\n')

    fptr.close()
