
"""
AGO !
fonction Size():enteir
debut
    repeter
        ecrire('Enter the size')
        lire(n)
    jusqua 2<=n<=15
    retourner n
fin
TDOL{
    n:entier
}

"""


def Size():
    while(1):
        n = int(input("Enter the size "))
        if n in range(2, 16):
            return n


def isPol(string: str):
    rev = ""
    counter = len(string)-1
    while(counter != 0):
        rev = string[counter]
        counter -= 1
    if(rev == string):
        return True
    return False


def fillMath(mat: list, size: int):
    line = []
    for i in range(size):
        for j in range(size):
            while(1):
                entry = input("Enteer thee caracter ")
                if(len(entry) == 1 and entry.isupper()):
                    break
            line.append(entry)
        mat.append(line)


def fillFile(mat: list, size: int):
    myFile = open("sym.txt", "w")
    lines = [[], 0]
    colms = [[], 0]
    myString = ""
    for i in range(size):
        for j in range(size):
            myString =
