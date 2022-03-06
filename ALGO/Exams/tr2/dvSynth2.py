from itertools import filterfalse
import numpy as np


def size(minimum: int, maximum: int):
    n = int(input("Enter The Size ! "))
    if minimum <= n <= maximum:
        return n
    return size(minimum, maximum)


def fillMatrix(matrix: np.ndarray, l: int, c: int):
    myFile = open("toCrypt.txt", "r")
    i = 0
    j = 0
    quit = False
    while not quit:
        try:
            line = myFile.readline()
            for k in range(len(line)):
                if line[k] == "\n":
                    matrix[i, j] = "#"
                else:
                    matrix[i, j] = line[k]
                j += 1
                if j == len(line)-1:
                    j = 0
                    i += 1
            print(i, j)
        except:
            quit = True
    while i < l and j < c:
        matrix[i, j] = "*"
        if j == c:
            j = 0
            i += 1
        else:
            j += 1

    myFile.close()


theSize = size(7, 10)
matrix = np.zeros([theSize, theSize], dtype=str)
fillMatrix(matrix, theSize, theSize)
print(matrix)
