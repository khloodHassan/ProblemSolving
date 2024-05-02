import math


def movingTiles(l, s1, s2, queries):
    # Write your code here
    speed = abs(s1 - s2)
    arr = []
    for query in queries:
        distance = math.sqrt(pow(l, 2) + pow(l, 2)) - math.sqrt(pow(math.sqrt(query), 2) + pow(math.sqrt(query), 2))
        arr.append((distance / speed))
    return arr


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    l = int(first_multiple_input[0])

    s1 = int(first_multiple_input[1])

    s2 = int(first_multiple_input[2])

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)
    print(result)


