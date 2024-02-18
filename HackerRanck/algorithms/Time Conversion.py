#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    time_list = s.split(':')
    first_part = time_list[0]
    last_part = time_list[-1]
    if first_part == '12' and time_list[-1][-2] == 'A':
        time_list[0] = '00'
    elif first_part != '12' and time_list[-1][-2] == 'P':
        first_part = str(int(time_list[0]) + 12)
        time_list[0] = first_part
    if time_list[-1][-2] == 'A':
        last_part = last_part.replace('AM','')
        time_list[-1] = last_part
    else:
        last_part = last_part.replace('PM', '')
        time_list[-1] = last_part

    return ":".join(time_list)

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
