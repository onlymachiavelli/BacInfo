

def divTwo(n: int):
    return int(str(n)[len(str(n))-1]) % 2 == 0


def det(n: int):
    chaine = str(n)
    longeur = len(chaine)
    lastIndex = int(chaine[longeur-1])
    return lastIndex % 2 == 0


def divThree(n: int):
    myString = str(n)
    summ = 0
    for i in range(len(myString)):
        summ += int(myString[i])
    return summ % 3 == 0


def divFour(n: int):
    return int(str(n)[len(str(n))-2: len(str(n))]) % 4 == 0


def divFive(n: int):
    return int(str(n)[len(str(n))-1]) == 0 or int(str(n)[len(str(n))-1]) == 5


print
