#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    inserted_num =arr[-1]
    for i in reversed(range(n)):
        if arr[i-1] > inserted_num:
            arr[i] = arr[i-1]
            if i == 0:
                arr[i] = inserted_num
                print(' '.join(str(num) for num in arr))
                break
            print(' '.join(str(num) for num in arr))
        else:
            arr[i] = inserted_num
            print(' '.join(str(num) for num in arr))
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
