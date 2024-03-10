

def activityNotifications(expenditure, d):

    expenditure.sort()
    num_of_Notifications = 0
    i = 0
    j = d
    while(j < (len(expenditure)-1)):
        arr = expenditure[i:j]
        if len(arr)% 2 ==0:
            median = (arr[int(len(arr)/2)] + arr[(int(len(arr)/2)) -1])/2
        else:
            median = arr[int(len(arr)/2)]
        if (median * 2)<= expenditure[j+1]:
            num_of_Notifications += 1
        i += 1
        j += 1
    return num_of_Notifications







if __name__ == '__main__':
    n = 0
    # d = 5
    #expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 5
    expenditure = [2,2,2,2,2]
    print(activityNotifications(expenditure, d))
    #print( expenditure[0:4])



