#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    num_val=0
    steps=0
    flag=0
    for i in range(0,n):
        if steps==0:
            if s[i]=="D":
                flag=1
                steps=steps-1
            elif s[i]=="U":
                flag=0
                steps=steps+1
        else:
            if s[i]=="D":
                steps=steps-1
            elif s[i]=="U":
                steps=steps+1
        if steps==0:
            if flag==1:
                num_val=num_val+1
            else:
                num_val=num_val
    return num_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
