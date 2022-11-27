#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    nameList = re.split(r'(\s+)', s)

    for i in range(len(nameList)):
        name = nameList[i];
        if name[0].isdigit() != True:
            nameList[i] = name.capitalize()
    
    listToStr = ''.join([str(elem) for elem in nameList])
    
    return listToStr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
