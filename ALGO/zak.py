import random as r


def Check(myString: str, n: int, ele: str):
    if n > 0:
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
        quit = not word.isupper()
    return word


def genAlpha():
    alpha = "abcdefghijjklmnopqrstuvwxyz"
    newAlpha = ""
    for i in range(26):
        quit = False
        while not quit:
            st = alpha[r.randint(0, 25)]
            quit = Check(newAlpha, i, st)
        newAlpha += st
    return newAlpha


def secretHash():
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


def result(word: str, alpha: str, secret: str):
    cryptedWord = ""
    for i in range(len(word)):
        for j in range(len(alpha)):
            if word[i] == alpha[j]:
                cryptedWord += secret[j]
    return cryptedWord


word = word()
print(f"the word is {word}")

alpha = genAlpha()
print(f"the alpha is {alpha}")
secret = secretHash()
print(f"the secret is {secret}")
print(result(word, alpha, secret))
