

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(candles):
    candles.sort(reverse=True)
    count_of_candles = 1
    tallest_candle = candles[0]
    for i in range(1, len(candles)):
        if candles[i] == tallest_candle:
            count_of_candles += 1
            if i == len(candles)-1:
                return count_of_candles
        else:
            return count_of_candles
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
