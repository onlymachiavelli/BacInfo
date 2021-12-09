import random as r

import numpy as np


l = r.randint(2, 10)
c = r.randint(2, 10)


def exist(l, c, m, n):
    for i in range(c):
        if n == m[l][i]:
            return True

    return False


def fillMat(l, c, m):
    for i in range(l):
        for j in range(c):
            while True:
                num = r.randint(-99, 100)
                if(not exist(i, j, m, num)):
                    break
            m[i][j] = num


def fillFile(l, c, m):
    for i in range(l):
        s1 = 0
        s2 = 0
        j = 0


m = np.zeros([l, c], dtype=int)
fillMat(l, c, m)
print(m)
