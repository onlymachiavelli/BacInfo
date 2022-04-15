import numpy as np
import pickle


def size():
    n = int(input("Enter Size ! "))
    if 1 < n < 20:
        return n
    return size()


def divElv(num):
    chaine = str(num)
    pair = 0
    imppair = 0
    for i in range(len(chaine)):
        if (i % 2 == 0):
            pair += int(chaine[i])
        else:
            imppair += int(chaine[i])

    return abs(pair-imppair) == 11


def getN(char: str):
    if char.isnumeric():
        return int(char)
    else:
        return ord(char) - 55


def toDec(code: str, base: int, i: int, j: int = 0):
    if i >= 0:
        return (getN(code[j])*(base**i)) + toDec(code, base, i-1, j+1)
    return 0


def fillFile(src, n):
    myFile = open(src, "w")

    for i in range(n):
        quit = False
        res = True
        while not quit:
            code = input("Enter code " + str(i))
            quit = len(code) <= 6 and code.isupper()
        myFile.write(code + "\n")
    myFile.close()


def filter(s):
    res = ""
    for i in range(len(s)):
        if s[i].isalpha():
            if "A" <= s[i] <= "F":
                res += s[i]
        else:

            res += s[i]
    return res


def binary(src, n):
    txt = open("chaine.txt", "r")
    arr = np.zeros(n, dtype=object)

    for i in range(n):
        line = filter(txt.readline()[0:-1])
        dec = toDec(line, 16, len(line)-1)
        nsg = ""
        if (divElv(dec)):
            nsg = "est divisinle par 11"
        else:
            nsg = "n'est pas divisinle par 11"

        arr[i] = {
            "Nb_Hex": line,
            "Nb_Dec": dec,
            "Div11": nsg
        }
    txt.close()
    myFile = open(src, "wb")
    for i in range(n):
        pickle.dump(arr[i], myFile)

    myFile.close()


def show(src, n):
    myFile = open(src, "rb")
    for i in range(n):
        print(pickle.load(myFile))
    myFile.close()


n = size()
src = "chaine.txt"
fillFile(src, n)
binary("res.dat", n)
show("res.dat", n)
