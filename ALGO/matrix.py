import numpy as np
import random as r

from numpy.core.fromnumeric import sort
# to show the matrix , stupid i know


def ShowMatr(matr, w: int, h: int):
    for i in range(h):
        for j in range(w):
            print(matr[i][j], end=" ,")
        print("\n")

# sorting matrice with arr


def Arrm(matr, w: int, h: int):
    arr = np.arange(w*h, dtype=int)
    # three loops lmao i know its stupid but our government  program ! fck em
    for l in range(w*h):
        for i in range(h):
            for j in range(w):
                arr[l] = matr[i][j]
    sorted(arr)  # sort that MF !
    print(arr)


matr1 = np.zeros([r.randint(3, 7), r.randint(3, 7)], dtype=int)
# just filling it ! randomly
h = matr1.size // len(matr1[0])  # got the Height
w = matr1.size // h  # Got the width
for i in range(h):
    for j in range(w):
        matr1[i][j] = r.randint(1, 100)

print(f"width = {w} and height = {h}")
ShowMatr(matr1, w, h)
Arrm(matr1, w, h)
