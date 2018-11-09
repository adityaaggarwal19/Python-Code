#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    res=[0,0]
    min_count=0
    max_count=0
    mi=scores[0]
    ma=scores[0]
    for i in range(0,len(scores)):
        if mi>scores[i]:
            mi=scores[i]
            min_count=min_count+1
        if ma<scores[i]:
            ma=scores[i]
            max_count=max_count+1
    res[0]=max_count
    res[1]=min_count
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
