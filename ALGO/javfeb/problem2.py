import numpy as np


def size(msg: str):
    print("Enter the ", msg)
    n = int(input())
    if 4 < n < 20:
        return n
    return size(msg)


def fillMat(mat: np.ndarray, n: int, i: int = 0, j=0):
    if i < n or j < n:
        return 0
