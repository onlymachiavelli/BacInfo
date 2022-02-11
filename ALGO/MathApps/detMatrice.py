from re import L
import numpy as np


def size():
    n = int(input("Enter the size"))
    if n > 2:
        return n
    return size()


def fillMath(mat: any, n: int):
    for i in range(n):
        for j in range(n):
            mat[i, j] = int(input("Enter Matrice"))
