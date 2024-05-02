import math

def connectingTowns(n, routes):
    return math.prod(routes) % 1234567




if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)
        print(result)