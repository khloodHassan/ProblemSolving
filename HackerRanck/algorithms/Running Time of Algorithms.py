

def runningTime(l):
    total_shift =0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           total_shift += 1
        l[j+1] = key
    return total_shift
if __name__ == '__main__':
    m = int(input().strip())
    ar = [int(i) for i in input().strip().split()]
    result = runningTime(ar)
    print(result)