#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
#https://www.hackerrank.com/challenges/a-very-big-sum/problem
def aVeryBigSum(ar):
    sum1=0
    for i in range(0,ar_count):
        sum1+=ar[i]
    return sum1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
