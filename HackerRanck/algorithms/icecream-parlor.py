






def icecreamParlor(m, arr):
    # Write your code here
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                return[i+1, j+1]





if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)
        print(result)


