




def balancedSums(arr):
    leftsum, rightsum = 0, sum(arr)
    # Write your code here
    for i in range(0, len(arr)):
        rightsum -= arr[i]
        if rightsum == leftsum:
            return 'YES'
        leftsum += arr[i]
    return 'NO'




if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = balancedSums(arr)
    print(result)