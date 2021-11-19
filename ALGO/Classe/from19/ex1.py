"""
Algorythm ex {
    Debut
        saisir(n)
        src <- "source.txt"
        remplir (src, n)
        genererM(src, n, m)
        triN(m,n)
        src1 <- "source1.txt"
        generer(src , m, n)
        
    Fin
}

"""

import random as r
import numpy as np
from numpy.lib.index_tricks import mgrid


def saisir():
    global n
    quit = False
    while not quit:
        n = int(input("Enter n "))
        quit = n in range(3, 16)


def remplirS(n, src):
    f = open(src, "w")
    for i in range(n):
        quit = False
        while not quit:
            lg = input("Enter Number structure ")
            quit = lg.isnumeric()
        f.write(lg+"\n")


def remplireMat(src, n, m):
    myFile = open(src, "r")
    lines = myFile.readlines()
    for i in range(n):
        mf = lines[i][0:len(lines[i])-1]
        print(mf)
        while len(mf) < n:
            random = str(r.randint(0, 10))
            print(random)
            mf = random + mf
            print("\n")
            print(mf)
        for j in range(n):
            m[i][j] = mf[j]

        # PP
n = 0

saisir()

m = np.array([[""]*n]*n, dtype=str)
src0 = "source0.txt"

remplirS(n, src0)

remplireMat(src0, n, m)
