
def countingSort(arr):
    result = [0] * 100
    # Write your code here
    for i in arr:
        result[i] += 1
    sorted_arr = list()
    for j in range(0,100):
        sorted_arr += ([j] * result[j])
    return sorted_arr

if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(result)