
import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:

        if grade < 40 and (math.ceil(grade / 5) * 5) != 40:
            result.append(grade)
        elif (math.ceil(grade / 5) * 5) - grade < 3 :
            result.append((math.ceil(grade / 5) * 5))
        else:
            result.append(grade)
    return result


if __name__ == '__main__':

    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)


