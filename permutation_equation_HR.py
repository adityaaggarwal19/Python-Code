#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    res=[0]*len(p)
    for i in range(0,len(p)):
        x=i+1
        y=0
        for j in range(0,len(p)):
            if p[j]==x:
                y=j+1
        for k in range(0,len(p)):
            if p[k]==y:
                res[i]=k+1
    return res
    
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
