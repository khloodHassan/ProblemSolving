

import math

def restaurant(l, b):
    # Write your code here
    square_len = 2
    print(math.gcd(l, b))
    return int((l * b) / pow(math.gcd(l, b), 2))
    # while(True):
    #    result = (l*b)/(square_len*square_len)
    #   if ((l*b)%(square_len*square_len)==0):
    #      return int(result)
    #  square_len += 1

if __name__ == '__main__':


    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = restaurant(l, b)
        print(result)