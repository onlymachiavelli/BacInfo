import numpy as np
import random as r


def exist(l, c, m, num):

    if len(m[l]) > 0:
        if num in m[l]:
            return True
    return False


def fillMat(l, c, m):
    for i in range(l):
        for j in range(c):
            quit = True
            while quit:
                num = r.randint(-99, 100)
                quit = exist(l, c, m, num)
            m[i][j] = num


l = r.randint(2, 11)
c = r.randint(2, 11)
m = np.zeros([l, c], dtype=int)
fillMat(l, c, m)


print(m)
