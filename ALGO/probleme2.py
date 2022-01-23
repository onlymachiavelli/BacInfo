import random as r
import numpy as np


def size():
    print("Enter N")
    n = int(input())
    if 4 < n < 20:
        return n
    return size()


def isPrime(n: int, i: int = 2):
    if n > 1:
        if i <= n//2:
            if n % i != 0:
                return isPrime(n, i+1)
            else:
                return False
        return True
    else:
        return False


def fillMat(n: int, mat, i: int = 0, j: int = 0):
    if i < n and j < n:
        num = r.randint(2, 99)
        columnIndex = j
        LineIndex = i
        if j == n-1:
            columnIndex = 0
            LineIndex = i+1
        else:
            columnIndex = j+1
        if isPrime(num):
            mat[i][j] = num
            fillMat(n, mat, LineIndex, columnIndex)
        else:
            fillMat(n, mat, i, j)


def isSorted(m, n: int, l: int, isLine: bool):
    j = 0
    checkIncr = True
    checkDecr = True
    theString = ""
    while j < n-1:
        if isLine:
            First = m[l][j]
            Then = m[l][j+1]
        else:
            First = m[j][l]
            Then = m[j+1][l]
        if First > Then:
            checkDecr = False
        else:
            checkIncr = False
        if checkIncr or checkDecr:
            theString += str(First) + "-"
        else:
            theString = ""
        j += 1
    return theString


def showFile(src: str, size: int):
    myFile = open(src, "r")
    for i in range(size):
        print(myFile.readline())
    myFile.close()


def genResult(m, n: int, src: str, i: int = 0):
    global counter
    if i < n:
        myFile = open(src, "a")
        if len(isSorted(m, n, i, False)) > 0:
            myFile.write("C" + str(i) + "*" + isSorted(m,
                         n, i, False) + str(m[i][n-1])+"\n")
            counter += 1
        if len(isSorted(m, n, i, True)) > 0:
            myFile.write("L" + str(i) + "*" + isSorted(m,
                         n, i, True) + str(m[n-1][i])+"\n")
            counter += 1
        myFile.close()
        genResult(m, n, src, i+1)


counter = 0
n = size()
mat = np.zeros([n, n], dtype=int)
fillMat(n, mat)
genResult(mat, n, "result.txt")
print(mat)
showFile("result.txt", counter)
