from unicodedata import decimal
import numpy as np


def size(minimum: int, maximum: int):
    n = int(input("Enter N "))
    if minimum < n < maximum:
        return n
    return size(minimum, maximum)


def fromDecimal(code: int, base: int):
    if code >= 0:
        return str(code % base) + fromDecimal(code // base, base)
    return ""


def readMessage(n: int, m: int, mat: np.ndarray):
    myFile = open("message.txt", "r")
    lines = myFile.readlines()

    myFile.close()
