#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p=0
    n=0
    z=0
    tf=len(arr)
    for i in range(0,len(arr)):
        if arr[i]>0:
            p=p+1
        elif arr[i]<0:
            n=n+1
        else:
            z=z+1
    print(format(p/tf,'.6f'))
    print(format(n/tf,'.6f'))
    print(format(z/tf,'.6f'))
    return 0

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
