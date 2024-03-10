

def findMedian(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        median = (arr[int(len(arr)/2)] + arr[(int(len(arr)/2)) -1])/2
    else:
        median = arr[int(len(arr)/2)]
    return int(median)



if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)
    print(result)