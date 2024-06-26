
import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here

    if year <= 1917:
        if year % 4 == 0:
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)

    elif year >= 1919:
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)
    else:
        return "26.09." + str(year)


if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)

