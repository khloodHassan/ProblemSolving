


#https://www.hackerrank.com/challenges/recursive-digit-sum/problem

def superDigit(n, k):
    sum = 0
    for i in n:
        sum += int(i)
    sum *= k
    def rec_solve(x):
        if len(x) == 1:
            return x
        sum = 0
        for i in x:
            sum += int(i)
        x = str(sum)
        return rec_solve(x)
    res = rec_solve(str(sum))
    return res

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    res = superDigit(n, k)
    print('res', res)


