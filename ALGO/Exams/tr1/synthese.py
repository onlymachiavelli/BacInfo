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


values = input("Enter the lengths ").split()
while True:
    l, c = map(int, values)
    if (userCheck(l, c)):
        break
mat = np.zeros([l, c], dtype=int)
fillMat(mat, l, c)

print(mat)

print(type(mat))
