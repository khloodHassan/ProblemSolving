


def countSort(arr):
    mid_index = len(arr) / 2
    helper_arr = [[]] * int(mid_index +1)
    for i in range(0,int(mid_index)):
        arr[i][1] = '-'
    for j in arr:
        print(len(helper_arr[j[0]]))
        if len(helper_arr[j[0]]) == 0:
            helper_arr[j[0]] = [j[1]]
        else:
            helper_arr[j[0]] += [j[1]]
    # for i in range(0,len(arr)):
    #  key = arr[i][0]
        #  char = arr[i][1]
        #  j = i - 1
        # while (j >= 0 and arr[j][0] > key):
    #  arr[j + 1] = arr[j]
            #   j -= 1
        # arr[j + 1] = [key,char]

    # for i in range(0, len(arr)):
    # if len(helper_arr[i]) == 0:
    #   helper_arr[i] = [arr[i][1]]
            # else:
    #  helper_arr[i] += [arr[i][1]]

    print(helper_arr)


if __name__ == '__main__':
    # arr =[[0,'a'],[1,'b'],[0,'c'],[1,'d']]
    # fun(arr, 4)
    arr = [[0, 'ab'], [6, 'cd'], [0, 'ef'], [6,'gh'],[4,'ij'], [0, 'ab'],[6, 'cd'],[0, 'ef'],[6, 'gh'],[0,'ij'],[4, 'that'],[3, 'be'],
[0, 'to'],
[1, 'be'],
[5, 'question'],
[1, 'or'],
[2, 'not'],
[4, 'is'],
[2, 'to'],
[4, 'the']]
    fun(arr, 20)

    #    arr = [[]] * 100
   #   print(len(arr[0]))
   #   arr[0] += [6]
   #   arr[1] = [2]
   #   arr[1] += [7]
   #   print(arr)
    # n = int(input().strip())
# arr = list(map(int, input().rstrip().split()))









