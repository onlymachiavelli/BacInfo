import numpy as np
import random as r
def size():
    quit = False
    while not quit:
        n = int(input("Give N "))
        quit = 20 < n < 120
    return n


def Range(msg: str):
    quit = False
    while not quit:
        num = int(input("Enter Num  " + msg))
        quit = -100 <= num <= 100
    return num


def trouve(t, n: int, num: int):
    test = False
    i = 0
    while not test and i < n:
        test = t[i] == num
        i += 1
    return test


def remplir(n: int, minn: int, maxx: int, t):
    for i in range(n):
        quit = True
        while quit:
            num = r.randint(minn, maxx)
            quit = trouve(t, i, num)
        t[i] = num


n = size()
arr = np.zeros(n, dtype=int)


print(arr)
quit = False

while not quit:
    minn = Range("min")
    maxx = Range("max")
    print(maxx > minn)
    print(maxx - minn)
    quit = maxx > minn and maxx-minn >= n

remplir(n, minn, maxx, arr)

print(arr)
