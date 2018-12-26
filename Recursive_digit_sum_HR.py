#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    n=str(n)
    a=""
    for i in range(0,k):
        a=a+n
    a=int(a)
    while a>9:
        a=supSum(a)
    return a
def supSum(p):
    if p>=0 and p<=9:
        return p
    else:
        return (p%10)+supSum(p//10) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
