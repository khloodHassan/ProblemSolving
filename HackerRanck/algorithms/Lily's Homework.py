


def lilysHomework(arr):
    i = 0
    j = len(arr) - 1
    min_swap = 0
    while (i< j):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            min_swap += 1
        else:
            j -= 1
    return min_swap







if __name__ == '__main__':
    arr = [4, 6, 7, 3]
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)
    print(result)


