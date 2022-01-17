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


def Fact(n: int, i: int = 2):
    if n == 1:
        return ""
    if n % i != 0:
        return Fact(n, i+1)
    else:
        return str(i) + Fact(n/i, i)


print(Fact(1912))


def fillRes(src: str, n: int, i: int = 0):
    if i < n:
        myFile = open(src, "w")
