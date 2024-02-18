#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[0:4])
    max_sum = sum(arr[1:5])
    print(min_sum, max_sum)

    # Write your code here


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
