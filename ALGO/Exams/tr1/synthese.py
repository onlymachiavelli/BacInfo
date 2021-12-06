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

                if(not exist()):
                    break


m = np.zeros([l, c], dtype=int)

print(m)
