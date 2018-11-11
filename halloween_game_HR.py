#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    if s>p:
        
        cost=p
        count=1
        s=s-p
        while s>0:
            if cost>m:
                cost=cost-d
                if cost<m:
                    cost=m
                s=s-cost
                if s>=0:
                    count=count+1
            else:
                cost=cost
                s=s-cost
                if s>=0:    
                    count=count+1
                else:
                    break
    else:
        count=0
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
