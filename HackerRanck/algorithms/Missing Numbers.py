
def missingNumbers(arr, brr):
    for x in arr:
        brr.remove(x)
    brr = list(set(brr))
    brr.sort()
    return brr








if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)
    print(result)