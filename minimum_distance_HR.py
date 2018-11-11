#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    mi=10000
    for i in range(0,len(a)):
        m=a[i]
        for j in range(i+1,len(a)):
            if m==a[j]:
                d=abs(i-j)
                if mi>d:
                    mi=d
    if mi==10000:
        mi=-1
    return mi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
