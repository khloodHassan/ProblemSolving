#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
# https://www.hackerrank.com/challenges/the-power-sum/problem

def powerSum(X, N):
    # Write your code here
    def rec_solve(x, n, start=1):
        if x==0:
            return 1
        i=start
        res=0
        while i**n<=x:
            res+=rec_solve(x-i**n, n, i+1)
            i += 1
        return res
    final_res = rec_solve(X,N)
    return final_res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
