import numpy as np
import random as r


def saisir():
    n = int(input("Entrer N"))
    if 4 < n < 20:
        return n
    else:
        return saisir()


def estPremier(n, i):
    if n > 1:
        if i <= n//2:
            if n % i != 0:
                return estPremier(n, i+1)
            else:
                return False
        return True
    else:
        return False


def remplir_m(m, n):
    for i in range(n):
        for j in range(n):
            quit = False
            while not quit:
                m[i][j] = r.randint(2, 99)
                quit = estPremier(m[i][j], 2)


def seq_ligne(m, n, l):
    i = 1
    testCroi = True
    testDecroi = True
    while i < n:
        if m[l][i] > m[l][i-1]:
            testDecroi = False
        else:
            testCroi = False
        i += 1
    return testCroi or testDecroi


def seq_col(m, n, l):
    testCroi = True
    testDecroi = True
    i = 1
    while i < n:
        if m[i][l] > m[i-1][l]:
            testDecroi = False
        else:
            testCroi = False
        i += 1
    return testCroi or testDecroi


def genererResultat(m, n, src):
    fs = open(src, "w")
    for i in range(n):
        # tester les lignes
        if seq_ligne(m, n, i):
            ch = "L"+str(i) + "*"
            for j in range(n):
                ch += str(m[i][j]) + "-"
            fs.write(ch[0:len(ch)-1] + "\n")
        if seq_col(m, n, i):
            ch = "C" + str(i) + "*"
            for j in range(n):
                ch += str(m[j][i]) + "-"
            fs.write(ch[0:len(ch)-1] + "\n")
    fs.close()


n = saisir()
m = np.zeros([n, n], dtype=int)
remplir_m(m, n)
print(m)
genererResultat(m, n, "result.txt")

"""
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
    while j <= n-2:
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


def genResult(m, n: int, src: str, i: int = 0):
    if i < n:
        myFile = open(src, "a")
        if len(isSorted(m, n, i, False)) > 0:
            myFile.write("C" + str(i) + "*" + isSorted(m,
                         n, i, False) + str(m[i][n-1])+"\n")
        if len(isSorted(m, n, i, True)) > 0:
            myFile.write("L" + str(i) + "*" + isSorted(m,
                         n, i, True) + str(m[i][n-1])+"\n")
        myFile.close()
        genResult(m, n, src, i+1)


n = size()
mat = np.zeros([n, n], dtype=int)
fillMat(n, mat)
print(mat)
genResult(mat, n, "result.txt")

"""
