import math

def lowestTriangle(trianglebase, area):
    # Write your code here
    return int(math.ceil((2*area)/trianglebase))

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    trianglebase = int(first_multiple_input[0])

    area = int(first_multiple_input[1])

    height = lowestTriangle(trianglebase, area)
    print(height)
