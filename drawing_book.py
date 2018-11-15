#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    min_s=0
    min_e=0
    min_s=(p//2)
    if n%2!=0:
        d=abs(n-p)
        min_e=(d//2)
    else:
        d=abs(n-p)
        if d%2==0:
            min_e=(d//2)
        else:
            min_e=(d//2)+1
    res=min(min_e,min_s)
    return res
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
