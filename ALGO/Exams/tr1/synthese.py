import random as r
from pickle import *
import numpy as np


def userCheck(l: int, c: int):
    if (l not in range(3, 11) and c not in range(3, 11)):
        return False
    return True


def exist(m: np.ndarray, l: int, c: int, num: int):
    if (c > 0):
        for i in range(c):
            if m[l][i] == num:
                return True
    return False


def fillMat(m: np.ndarray, l: int, c: int):
    for i in range(l):
        for j in range(c):
            while True:
                num = r.randint(-99, 100)
                if (not exist(m, i, j, num)):
                    break
            m[i][j] = num


def fillDat(m: np.ndarray, l: int, c: int):

    for i in range(l):
        k = 1
        s0 = 0
        s1 = 0
        while True:
            for j in range(k):
                s0 += m[i][j]
            for j in range(k+1, c):
                s1 += m[i][j]
            
            k += 1
            if (s0 == s1):
                print(s1)
            if (k == c-1 ):
                break
        


values = input("Enter the lengths ").split()
while True:
    l, c = map(int, values)
    if (userCheck(l, c)):
        break
mat = np.zeros([l, c], dtype=int)
fillMat(mat, l, c)
fillDat(mat, l, c)
print(mat)

print(type(mat))
