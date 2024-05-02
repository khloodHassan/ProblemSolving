


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    game_max_min_score =[scores[0], scores[0]]
    count_max_min = [0, 0]
    for i in range(1, n):
        if scores[i] > game_max_min_score[0]:
            game_max_min_score[0] = scores[i]
            count_max_min[0] += 1
        if scores[i] < game_max_min_score[1]:
            game_max_min_score[1] = scores[i]
            count_max_min[1] += 1

    return count_max_min




if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
