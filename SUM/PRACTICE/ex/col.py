import numpy as np
import random as r


def size(mi, ma):
    n = int(input("Enteer N \n "))
    if mi <= n <= ma:
        return n
    return size(mi, ma)


def fillMat(mat, l, c):
    for i in range(l):
        for j in range(c):
            mat[i, j] = r.randint(1, 11)


def fillMin(mat, l, c, m):
    for i in range(l):
        mini = {"i": i, "j": 0}
        for j in range(c):
            if m[i, j] < m[mini["i"], mini["j"]]:
                mini["i"] = i
                mini["j"] = j
        mat[mini["i"], mini["j"]] = 1
        for j in range(c):
            if m[i, j] == m[mini["i"], mini["j"]]:
                mat[i, j] = 1


def fillMax(mat, l, c, m):
    for j in range(c):
        maxi = {"i": 0, "j": j}
        for i in range(l):
            if m[i, j] > m[maxi["i"], maxi["j"]]:
                maxi["i"] = i
                maxi["j"] = j
        mat[maxi["i"], maxi["j"]] = 1
        for i in range(l):
            if m[i, j] == m[maxi["i"], maxi["j"]]:
                mat[i, j] = 1


l = size(3, 20)
c = size(3, 20)

mat = np.array([[int()]*c]*l)
mini = np.array([[int()]*c]*l)
maxi = np.array([[int()]*c]*l)

fillMat(mat, l, c)
fillMin(mini, l, c, mat)
fillMax(maxi, l, c, mat)
print(maxi)
print(mat)
print(mini)
