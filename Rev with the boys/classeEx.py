from textwrap import fill
import numpy as np

import pickle


def getAllDatas(n: int):
    myFile = open("resul.dat", "rb")
    res = np.array([""]*n, dtype=str)
    for i in range(n):
        a = pickle.load(myFile)
        res[i] = a
    return res


def Number(maxx: int):
    quit = False
    while not quit:
        n = int(input("enter the number "))
        quit = 2 < n < maxx
    return n


def PrimeFac(n: int):
    quit = False
    d = 2  # First prime number
    res = np.array([""]*n, dtype=str)
    i = 0
    while not quit:
        if n % d == 0:
            n = n/d
            res[i] = str(d)
            i += 1

        else:
            d += 1
        quit = n == 1

    return res


def fillFile(n: int):
    myFile = open("resul.dat", "wb")
    p = Number(100)
    for i in range(n):
        quit = False
        while not quit:
            nb = int(input("Enter P "))
            quit = len(str(nb)) == p

        pickle.dump(str(nb), myFile)

    myFile.close()


def fillTxt(n: int):
    myFile = open("facteurs.txt", "w")
    res = getAllDatas(n)

    for i in range(n):
        t = PrimeFac(int(res[i]))
        freq = ""
        for j in range(len(t)):
            counter = 1
            for p in range(len(t)):
                if p != j:
                    if t[p] == t[j]:
                        counter += 1
            freq += str(counter) + t[j]
            print(t[j])
        myFile.write(freq + "\n")
    myFile.close()


n = Number(6)
fillFile(n)
fillTxt(n)
