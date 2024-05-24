





s1 = []
s2 = []

def enqueue(x):
    s1.append(x)


def dequeue():
    s2.extend(s1[:0:-1])
    s1.clear()
    s1.extend(s2[::-1])
    s2.clear()


def display():
    print(s1[0])


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        q = list(map(int, input().split()))
        if q[0] == 1:
            enqueue(q[1])
        elif q[0] == 2:
            dequeue()
        else:
            display()


