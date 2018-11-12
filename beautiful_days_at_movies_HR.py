#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count=0
    for a in range(i,j+1):
        b=a
        rev=0
        while(a!=0):
            r=a%10
            rev=rev*10+r
            a=a//10
        d=abs(rev-b)
        print("Rev",rev)
        if d%k==0:
            count=count+1
        else:
            count=count
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
