#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    space = n-1
    symbol = 1
    for i in range(0, n):
        print(' ' * space + '#' * symbol)
        space -= 1
        symbol += 1
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
