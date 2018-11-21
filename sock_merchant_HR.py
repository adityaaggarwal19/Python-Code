#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    cou=[0]*max(ar)
    po=0
    for i in range(0,len(ar)):
        cou[ar[i]-1]=cou[ar[i]-1]+1
    ma=cou[0]
    for i in range(0,max(ar)):
        d=cou[i]//2
        po=po+d
    return po

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
