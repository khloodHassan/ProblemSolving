

def closestNumbers(arr):
    arr.sort()
    min_val = arr[1] - arr[0]
    # Write your code here
    closest_num = list()
    closest_num.append(arr[0])
    closest_num.append(arr[1])
    for i in range(1, len(arr)):
        if i == len(arr)-1:
            break
        if arr[i+1] - arr[i] < min_val:
            closest_num = list()
            closest_num.append(arr[i])
            closest_num.append(arr[i+1])
            min_val = arr[i+1] - arr[i]
        elif arr[i+1] - arr[i] == min_val:
            closest_num.append(arr[i])
            closest_num.append(arr[i + 1])

    return closest_num

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    print(result)