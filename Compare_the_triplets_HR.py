#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    r=[0,0]
    n=len(a)
    for i in range(0,n):
        if a[i]>b[i]:
            r[0]= r[0]+1
        elif a[i]<b[i]:
            r[1]=r[1]+1
        else:
            r[1]=r[1]
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
