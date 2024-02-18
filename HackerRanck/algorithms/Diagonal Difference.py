#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
# https://www.hackerrank.com/challenges/diagonal-difference/problem
def diagonalDifference(arr):
    i1=0
    j2=n-1
    sum1=0
    sum2=0
    for k in arr:
        sum1+=k[i1]
        i1+=1
        sum2+=k[j2]
        j2-=1
    return(abs(sum1-sum2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
