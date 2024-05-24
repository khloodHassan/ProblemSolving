

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)
    indx1 = 0
    indx2 = 0
    indx3 = 0
    while(sum_h1 != sum_h2 or sum_h1 != sum_h3):
        if sum_h1>= sum_h2 and sum_h1 >= sum_h3:
            sum_h1 -=h1[indx1]
            indx1 +=1
        elif sum_h2 >= sum_h3:
            sum_h2 -=h2[indx2]
            indx2 +=1
        else:
            sum_h3 -=h3[indx3]
            indx3 += 1

    return sum_h1


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)
