#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
# https://www.hackerrank.com/challenges/plus-minus/problem
def plusMinus(arr):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in arr:
        if (i >= 1):
            count1 += 1
        elif (i < 0):
            count2 += 1
        else:
            count3 += 1

    print(round(count1 / n, 6))
    print(round(count2 / n, 6))
    print(round(count3 / n, 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
