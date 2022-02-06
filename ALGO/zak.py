import random as r
from tty import setcbreak


def check(myString: str, n: int, ele: str):
    check = True
    i = 0
    while check and i < n:
        check = not myString == ele
    i += 1
    return check


def word():
    quit = False
    while not quit:
        word = input("Enter the word ")
        quit = word.isupper()
    return word


def genAlpha():
    alpha = "abcdefghijjklmnopqrstuvwxyz"
    newAlpha = ""
    for i in range(26):
        quit = False
        while not quit:
            st = alpha[r.randint(0, 25)]
            quit = check(newAlpha, i, st)
        newAlpha += st
    return newAlpha


def secret():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    quit = False
    while not quit:
        secret = input("Enter Secret ")
        i = 0
        test = True
        while i < len(secret):
            if not check(secret, len(secret), secret[i]):
                test = False
            i += 1
        quit = test

    for i in range(len(secret), 26):
        quit = False
        while not quit:
            st = alpha[r.randint(0, 25)]
            quit = check(secret, len(secret), st)
        secret += st

    return secret


def result():
