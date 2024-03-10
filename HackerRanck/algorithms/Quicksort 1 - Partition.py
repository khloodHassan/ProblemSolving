
def quickSort(arr):
    povit = arr[0]
    arr_left, arr_right = list(), list()
    for i in arr:
        if i < povit:
            arr_left.append(i)
        elif i > povit:
            arr_right.append(i)
    arr_left.append(povit)
    return ' '.join(map(str,arr_left + arr_right))
    # Write your code here



if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    print(result)