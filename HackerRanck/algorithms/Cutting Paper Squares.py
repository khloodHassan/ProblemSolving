


def solve(n, m):
    # Write your code here
    return (n*m) - 1


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = solve(n, m)
    print(result)
