import numpy as np


def saisir():
    quit = False
    while not quit:
        n = int(input("Enter N"))
        quit = n >= 9

    return n


def verif(t, n, al):
    test = True
    if n > n:
        test = False
        minn = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        while i < 26:
            if (minn[i] == al):
                test = True
                i += 1
        i = 0
        while i < n and test:
            if t[i] == al:
                test = False
                i = n
            i += 1
        return test
    return test


def remplir(t, n):
    for i in range(n):
        quit = False
        while not quit:
            alpha = input("Enter alpha "+str(i))
            quit = len(alpha) == 1 and verif(t, n, alpha)
        t[i] = alpha


def saissir_m():
    quit = False
    while not quit:
        mot = input("Enter Word")
        quit = 0 < len(mot) <= 7
    return mot


def result(t, n, mot):
    res = ""
    counter = 0
    for i in range(n):
        for j in range(len(mot)):
            if t[i] == mot[j]:
                counter += 1
                res = res + str(i) + " "

    if counter != len(mot):
        res = "error ya haj "
    return res


n = saisir()
t = np.array(['']*n, dtype=str)
print(t)
remplir(t, n)
mot = saissir_m()

print(result(t, n, mot))
