import numpy as np
import random as r
import pickle


def size(msg: str, condition: int):
    print("Enter the ", msg)
    n = int(input())
    if 2 < n < condition:
        return n
    return size()


def fillFile(src: str, n: int, i: int = 0):
    if i < n:
        myFile = open(src, "wb")
        p = size("P")
        print("Enter the nubmer")
        numb = int(input())
        if numb != p:
            myFile.close()
            fillFile(src, n, i)
        else:
            pickle.dump(numb, myFile)
            myFile.close()
            fillFile(src, n, i+1)


def Fact(n: int, arr: list, i: int = 2):
    if n > 1:
        print(n)
        print(arr)
        if n % i != 0:
            Fact(n, arr, i+1)
        else:
            arr.append(i)
            Fact(n/i, i)


def Frequency(ch: list, c: int = 1, n: int = 0):
    if len(ch) > 0:
        if ch[n] == ch[n-1]:
            return Frequency(ch, c+1, n-1)
        else:
            return str(c)+ch[n-1] + Frequency(ch, 1, n-1)
    else:
        return ""


def fillRes(src: str, n: int, i: int = 0):

    if i < n:
        myFile = open(src, "w")


fa = []
print(Fact(1912, fa))

print(fa)
