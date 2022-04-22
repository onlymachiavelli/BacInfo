import numpy as np


def getSalt():
    salt = input("Entrez un salt : ")
    for i in range(len(salt)):
        count = 0

        for j in range(len(salt)):
            if salt[i] == salt[j]:
                count += 1
            if count > 1 or not salt.isupper() or 5 <= len(salt) <= 10:
                return getSalt()
    return salt


def crypt(salt, src):
    myFile = open(src, "r")
    res = open("crypt.txt", "w")
    quit = False
    while not quit:
        try:
            line = myFile.readlin()
            while len(line) % len(salt) != 0:
                line += " "

        except:
            quit = True
    res.close()
    myFile.close()


def show(src):
    myFile = open(src, "r")
    quit = False
    while not quit:
        try:
            print(myFile.readline())
        except:
            quit = True

    myFile.close()


print(getSalt())
