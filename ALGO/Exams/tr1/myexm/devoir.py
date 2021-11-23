import numpy as np
import random as r
import pickle


def size():
    myfile = open("source.txt", "r")
    quit = False
    n = 0
    while not quit:
        a = myfile.readline()
        if len(a) == 0:
            quit = True
        else:
            n += 1

    myfile.close()
    return n


def fillmat(n, m):
    myfile = open("source.txt", "r")

    for i in range(n):
        res = ""
        ch = myfile.readline()
        for j in range(len(ch)):
            if ch[j].isnumeric():
                res += ch[j]
        while len(res) < n:
            res += str(r.randint(0, 10))
        for j in range(n):
            m[i][j] = res[j]


def fillbin(n, m):
    mybin = open("maximum.dat", "wb")
    for i in range(n):
        mii = int(m[i][0])
        myj = 0
        for j in range(n):

            if int(m[i][j]) > mii:
                mii = int(m[i][j])
                myj = j
        pickle.dump({
            "max": mii,
            "cord": {
                    "nl": i,
                    "nc": myj
                    }
        }, mybin)


def mymax(n):
    mnn = []
    myfile = open("maximum.dat", "rb")
    datas = []
    for i in range(n):
        a = pickle.load(myfile)
        datas += [a]
    mx = datas[0]
    mn = datas[0]
    for i in range(n):
        if datas[i]["max"] > mx["max"]:
            mx = datas[i]
        if (mn["max"] > datas[i]["max"]):
            mnn += [datas[i]]
            mn = datas[i]
    print("the max")
    print(mx)  # the maximum (Last one)
    print("the min")
    print(mnn[0])  # The first minimum


n = size()
m = np.array([[""]*n] * n, dtype=str)
fillmat(n, m)
fillbin(n, m)
mymax(n)
