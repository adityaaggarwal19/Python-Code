#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    cou=[0]*max(arr)
    po=0
    for i in range(0,len(arr)):
        cou[arr[i]-1]=cou[arr[i]-1]+1
    ma=cou[0]
    for i in range(0,max(arr)):
        if cou[i]>ma:
            ma=cou[i]
            po=i+1
    return po

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
