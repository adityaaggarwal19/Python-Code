#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum=[0,0,0,0,0]
    sum[0]=arr[0]+arr[1]+arr[2]+arr[3]
    sum[1]=arr[0]+arr[4]+arr[2]+arr[3]
    sum[2]=arr[0]+arr[1]+arr[4]+arr[3]
    sum[3]=arr[0]+arr[1]+arr[2]+arr[4]
    sum[4]=arr[4]+arr[1]+arr[2]+arr[3]
    mi=min(sum)
    ma=max(sum)
    print(mi,ma)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
