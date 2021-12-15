import random as r

import numpy as np
from pickle import *


def exist(l, c, m, n):
    for i in range(c):
        if n == m[l][i]:
            return True
    return False


def SelectionSort(n, t):
    for i in range(n-1):
        j = i
        tmp = t[i]
        while j >= 1 and tmp.n < t[j]


def fillMat(l, c, m):
    for i in range(l):
        for j in range(c):
            while True:
                num = r.randint(-99, 100)
                if(not exist(i, j, m, num)):
                    break
            m[i][j] = num


def fillFile(l, c, m):
    myFile = open("file.dat", "w")
    for i in range(l):
        s1 = 0
        s2 = 0
        su = False
        j = 0
        while j != c-1 or not su:
            s2 = 0
            j += 1
            s1 += m[i][j]

            for k in range(j+1, c):
                s2 += m[i][k]
            su = s1 == s2
        print(su)


l = r.randint(2, 10)
c = r.randint(2, 10)

m = np.zeros([l, c], dtype=int)
fillMat(l, c, m)
fillFile(l, c, m)
print(m)
