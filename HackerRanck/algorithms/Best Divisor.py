import math
import os
import random
import re
import sys


def bestDivisor(n):
    sum = 0
    max_num = 0
    best_divisor = 0
    for i in range(1,n+1):
        if n%i == 0:
           k = i
           while(k>0):
               sum += (k%10)
               k = k//10
        if max_num < sum:
            max_num = sum
            best_divisor = i

        sum = 0

    print(best_divisor)



if __name__ == '__main__':
    n = int(input().strip())
    bestDivisor(n)

