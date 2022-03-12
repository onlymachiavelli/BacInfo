

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


def divNine(n):
    # assuming that n is bigger than 100 !
    number = int(str(n)[0]) + int(str(n)[1])

    for i in range(2, len(str(n))):
        if number >= 9:
            number -= 9
        number += int(str(n)[i])

    return number - 9 == 0


def divTen(n: int):
    return int(str(n)[len(str(n))-1]) == 0


def divTFive(n: int):
    return int(str(n)[len(str(n)-2):len(str(n)-1)]) % 25 == 0


def divStuff(number: str):
    struct = number
    while len(struct) % 4 != 0:
        struct = "0" + struct
    num = ""
    arr = []
    for i in range(len(struct)):
        num += struct[i]
        if len(num) == 4:
            arr.append(num)
            num = ""
    res = 0
    cof = 1
    for i in range(len(arr)):
        res += int(arr[i]) * cof
        cof *= -1

    return res % 137 == 0


print(divStuff("2510792736157732104"))
