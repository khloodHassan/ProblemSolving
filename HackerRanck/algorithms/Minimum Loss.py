import math

def minimumLoss(price):
    # Write your code here
    min_loss = 10000000000000000
    for p in range(0,len(price)-1):
        for i in range(p+1,len(price)):
            if price[p] - price[i] < min_loss and price[p] - price[i] >= 0:
                min_loss = price[p] - price[i]
    return min_loss

def minimumLoss(price):
    # Write your code here
    sortedPrice=sorted([(p,idx) for idx,p in enumerate(price)])
    minLoss=math.inf
    n=len(sortedPrice)
    for i in range(1,n):
        if sortedPrice[i][1]<sortedPrice[i-1][1]:
            minLoss=min(minLoss,sortedPrice[i][0]-sortedPrice[i-1][0])
    return minLoss
if __name__ == '__main__':

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)
    print(result)