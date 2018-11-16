#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count=0
    i=c[0]
    while i<len(c):
        if (i+2)<len(c):
            if c[i+2]==1:
                i=i+1
                count=count+1
            else:
                i=i+2
                count=count+1
        else:
            if (i+1)<len(c):
                i=i+1
                count=count+1
            else:
                break
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
