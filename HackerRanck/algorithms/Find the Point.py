





def findPoint(px, py, qx, qy):
    # Write your code here
    rx = 2* qx - px
    ry = 2* qy - py
    return [rx,ry]


if __name__ == '__main__':
    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        px = int(first_multiple_input[0])

        py = int(first_multiple_input[1])

        qx = int(first_multiple_input[2])

        qy = int(first_multiple_input[3])

        result = findPoint(px, py, qx, qy)
        print(' '.join(map(str, result)))