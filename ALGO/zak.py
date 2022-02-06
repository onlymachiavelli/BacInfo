import random as r


def Check(myString: str, ele: str):
    check = True
    for i in range(len(myString)):
        if myString[i] == ele:
            check = False
    return check


def word():
    quit = False
    while not quit:
        word = input("Enter the word ")
        quit = not word.isupper()
    return word


def genAlpha():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    print(len(alpha))
    newAlpha = ""
    for i in range(26):
        quit = False
        while not quit:
            st = alpha[r.randint(0, 25)]
            quit = Check(newAlpha, st)
            print(quit)
        newAlpha += st
    return newAlpha


def dubl(myString: str, ele: str):
    count = 0
    for i in range(len(myString)):
        if myString[i] == ele:
            count += 1
    if count > 1:
        return False
    return True


def secretHash():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    quit = False
    while not quit:
        quit = True
        secret = input("Enter Secret ")
        for i in range(len(secret)):
            if secret[i].isupper() or not dubl(secret, secret[i]):
                quit = False
    for i in range(len(secret), 26):
        quit = False
        while not quit:
            st = alpha[r.randint(0, 25)]
            quit = Check(secret, st)
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
