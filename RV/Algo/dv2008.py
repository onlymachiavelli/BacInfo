import numpy as np
import random as r


def fillMat(mat):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(6):
        for j in range(6):
            mat[i][j] = alpha[r.choice(alpha)[0]]
