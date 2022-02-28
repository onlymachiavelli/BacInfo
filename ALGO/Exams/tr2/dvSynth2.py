import numpy as np


def size(minimum: int, maximum: int):
    n = int(input("Enter The Size ! "))
    if minimum < n < maximum:
        return n
    return size(minimum, maximum)


def fillMatrix(matrix: np.ndarray, l: int, c: int):
    myFile = open("toCrypt.txt", "r")
    i = 0
    j = 0
    check = False
    while i < l and j < c:
        line = myFile.readline()
        if line != None:
            check = False
        for k in range(len(line)):
            if line[k] == "\n":
                matrix[i, j] = "#"
            if j == c - 1:
                j = 0
                i += 1

    myFile.close()
