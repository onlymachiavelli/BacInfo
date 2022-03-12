def divTwo(n: int):
    return int(str(n)[len(str(n))-1]) % 2 == 0


def divThree(n: int, res: int = 0, i: int = 0):
    if i < len(str(n)):
        return divThree(n, res+int(str(n)[i]), i+1)
    return res % 3 == 0


def divFour(n: int):
    return int(str(n)[len(str(n))-2] + str(n)[len(str(n))-1]) % 4 == 0


def divFive(n: int):
    return int(str(n)[len(str(n))-1]) == 5 or int(str(n)[len(str(n))-1]) == 0


def divSix(n: int):
    return divTwo(n) and divThree(n)


def divSeven(n: int):
    if n < 100:
        return divSeven((int(str(n)[0:len(str(n))-2])) - (2*int(str(n)[len(str(n))-1])))
    return n % 7 == 0
