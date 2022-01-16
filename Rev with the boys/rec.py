import numpy as np
import random as r
import pickle
from math import sqrt


def size(msg):
    quit = False
    while not quit:
        n = int(input("Enter "+msg))
        quit = 4 < n < 13
    return n


def exist(mat, l, c, num):
    i = 0
    test = False
    while i < c and not test:
        test = num == mat[l][i]
        i += 1
    return test


def fillMat(mat, l, c):
    for i in range(l):
        for j in range(c):
            quit = False
            while not quit:
                num = r.randint(1, 50)
                quit = not exist(mat, i, j, num)
            mat[i][j] = num


def isPrime(n: int, i: int = 1):
    if i > sqrt(n):
        return True
    else:
        if n % i != 0:
            return True
        return isPrime(n, i+1)


def fillFile(mat, l, c):
    myFile = open("result.dat", "wb")
    arr = []
    for i in range(l):
        nop = 0
        summ = 0
        arr = []
        for j in range(c):
            if isPrime(mat[i][j]):
                print(mat[i, j])
                nop += 1
            else:
                arr += mat[i, j]
                print(arr)
        print(nop >= c//2)
        if nop > c//2:
            res = {
                "line ": i,
                "summOfLine": summ,
                "isSumPrime": isPrime(summ),
                "NonePrimaryList": arr
            }
            print(res)
            pickle.dump(res, myFile)
    myFile.close()


print(isPrime(3))

l = size("Lignes")
c = size("Columns")
mat = np.zeros([l, c], dtype=int)
fillMat(mat, l, c)
fillFile(mat, l, c)
print(mat)
