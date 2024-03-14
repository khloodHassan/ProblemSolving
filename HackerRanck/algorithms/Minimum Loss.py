import math


def minimumLoss(price):
    # Write your code here
    sortedPrice=sorted([(p, idx) for idx, p in enumerate(price)])
    minLoss=math.inf
    for i in range(1, len(sortedPrice)):
        if sortedPrice[i][1] < sortedPrice[i-1][1]:
            minLoss = min(minLoss,sortedPrice[i][0]-sortedPrice[i-1][0])
    return minLoss
if __name__ == '__main__':

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)
    print(result)