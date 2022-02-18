from asyncio.windows_events import NULL
from contextlib import nullcontext
from logging import NullHandler
import random as r
import readline
import numpy as np


def fillTextDec():
    global n
    myFile = open("dec.txt", "w")
    for i in range(r.randint(10, 30)):
        myFile.write(str(r.randint(90, 999)) + "\n")
        n += 1


def getN(char: str):
    return int(char)


def getS(num: int, base: int):
    if base == 16:
        alphas = np.zeros(16, dtype=str)
        alphas = ["0", "1", "2", "3", "4", "5", "6",
                  "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        i = -1
        found = False
        while not found:
            i += 1
            found = num == i
        return alphas[i]

    return str(num)


def fromDec(code: int, base: int):
    if code > 0:
        return fromDec(code // base, base) + getS(code % base)
    return ""


print(fromDec(740, 2))


def toDec(code: str, base: int, i: int, j: int = 0):
    if i >= 0:
        return (getN(code[j])*(base**i)) + toDec(code, base, i-1, j+1)
    return 0


def binaryConverter(src: str, n: int):
    source = open("dec.txt", "r")

    myFile = open(src, "w")
    for i in range(n):
        line = int(source.readline())
        myFile.write(fromDec(line, 2) + "\n")

    myFile.close()
    source.close()


def octaleConverter(src: str, n: int):
    myFile = open(src, "w")
    decFile = open("dec.txt", "r")
    for i in range(n):
        line = int(decFile.readline())
        myFile.write(fromDec(line, 8) + "\n")
    myFile.close()
    decFile.close()


def hexaConverter(src: str, n: int):
    myFile = open(src, "w")
    decFile = open("dec.txt", "r")
    for i in range(n):
        line = int(decFile.readline())
        myFile.write(fromDec(line, 16) + "\n")
    decFile.close()
    myFile.close()


n = 0

fillTextDec()
binaryConverter("bin.txt", n)
octaleConverter("octale,txt", n)
hexaConverter("hexa.txt", n)
