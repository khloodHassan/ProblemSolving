
import math


#def primeCount(n):
# return sum(math.prod([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53][:i+1]) <= n for i in range(16))
def primeCount(n):
    count = 0
    prime=2
    isPrime = True
    prod=1
    while (True):
        for i in range(2, int(math.sqrt(prime))+1):
            if prime % i == 0:
                isPrime = False
        if isPrime:
            prod = prod * prime
            count +=1
            if prod > n:
                count -= 1
                break
        prime+=1
        isPrime = True
    return (count)




if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)
        print(result)