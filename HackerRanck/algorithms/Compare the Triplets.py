#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
# https://www.hackerrank.com/challenges/compare-the-triplets/submissions/code/108504979
def compareTriplets(a, b):
    Alice=0
    Bob=0
    for i in range(0,3):
        if(a[i]>b[i]):
            Alice+=1
        elif(a[i]<b[i]):
            Bob+=1
    return[Alice,Bob]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
