


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

def lilysHomework(arr):
    def run(arr,reverse):
        index_dict = {}
        for i in range(len(arr)):
            index_dict[arr[i]] = i
        ans = 0
        arr_sort = sorted(arr,reverse = reverse)
        for i in range(len(arr)):
            if arr[i] != arr_sort[i]:
                ans+=1
                index_ = index_dict[arr_sort[i]]
                index_dict[arr[i]],index_dict[arr_sort[i]] = index_dict[arr_sort[i]],index_dict[arr[i]]
                arr[i],arr[index_] = arr[index_],arr[i]
        return ans
    return min(run(arr.copy(),True),run(arr.copy(),False))
def lilysHomework(arr):
    ans1 = ans2 = 0
    arr2 = arr.copy()
    temp1 = arr.copy()
    temp2 = arr.copy()
    n = len(arr)
    h = {}
    h2 = {}
    temp1.sort()
    temp2.sort()
    temp2.reverse()
    for i in range(n):
        h[arr[i]] = i
        h2[arr[i]] = i
    init = 0
    for i in range(n):
        if (arr[i] != temp1[i]):
            ans1 += 1
            init = arr[i]
            arr[i], arr[h[temp1[i]]] = arr[h[temp1[i]]], arr[i]
            h[init] = h[temp1[i]]
            h[temp1[i]] = i
    for i in range(n):
        if (arr2[i] != temp2[i]):
            ans2 += 1
            init = arr2[i]
            arr2[i], arr2[h2[temp2[i]]] = arr2[h2[temp2[i]]], arr2[i]
            h2[init] = h2[temp2[i]]
            h2[temp2[i]] = i
    return min(ans1, ans2)





if __name__ == '__main__':
    arr = [4, 6, 7, 3]
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)
    print(result)


