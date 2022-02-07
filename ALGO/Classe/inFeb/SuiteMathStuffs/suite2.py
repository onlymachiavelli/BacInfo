import random as r
import numpy as np
import pickle


def fillMatrice(myMatrice: any, l: int, c: int):
    alpha = "abcdefghijklmnopqrstuvwxyz".upper()
    for i in range(l):
        for j in range(c):
            myMatrice[i, j] = alpha[r.randint(0, 25)]


def size():
    n = int(input("Give me the size "))
    if 2 < n < 10:
        return n
    return size()


def count(mat: any, ele: str, l: int, c: int):
    count = 0
    for i in range(l):
        for j in range(c):
            if ele == mat[i, j]:
                count += 1
    return count


def isIn(t: any, n: int,  ele: str):
    count = 0
    for i in range(n):
        if ele == t[i]:
            count += 1
    return count <= 1


def suite(n: int, a: int, b: int):
    a = 1
    b = 2
    u = 0

    for i in range(3, n+1):
        u = round(3/2 * b) + 2*a
        a = b
        b = u
    return u


def genFile(myMatrice: any, l: int, c: int):
    myFile = open("myFile.dat", "wb")
    theT = np.zeros(26, dtype=str)
    n = 0
    for i in range(l):
        for j in range(c):
            if(isIn(theT, n, myMatrice[i, j])):
                n += 1
                pickle.dump({
                    "Char": myMatrice[i, j],
                    "Poid": suite(count(myMatrice, myMatrice[i, j], l, c,), 1, 2)
                }, myFile)
                print({
                    "Char": myMatrice[i, j],
                    "Poid": suite(count(myMatrice, myMatrice[i, j], l, c,), 1, 2)
                })


l = size()
c = size()

mat = np.zeros([l, c], dtype=str)

fillMatrice(mat, l, c)
genFile(mat, l, c)
