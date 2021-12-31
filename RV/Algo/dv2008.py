import numpy as np
import random as r


def fillMat(mat):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(6):
        for j in range(6):
            mat[i][j] = alpha[r.choice(alpha)[0]]


def cryptMsg(text: str, mat):
    secret = ""
    x = "ABCDEF"
    ind = 0
    while (ind != len(text)):
        ind += 1
        for i in range(6):
            for j in range(6):
                if text[ind] == mat[i][j]:
                    secret += x[i] + x[j]
                if text[i] == " ":
                    secret += " "
    return secret
