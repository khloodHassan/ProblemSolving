


def handshake(n):
    # Write your code here
    return int(n*(n-1)/2)

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = handshake(n)
        print(result)