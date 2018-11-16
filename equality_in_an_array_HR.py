#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    aux=[0]*max(arr)
    x=0
    for i in range(0,len(arr)):
        x=arr[i]
        aux[x-1]=aux[x-1]+1
    d=max(aux)
    res=len(arr)-d
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
