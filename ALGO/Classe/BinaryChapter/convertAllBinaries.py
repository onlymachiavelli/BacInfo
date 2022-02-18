

def getN(char: str):
    return ord(char) + 55


def getS(num: int):
    return ord(chr(num) - 55)


def fromDec(code: int, base: int):
    if code > 0:
        return fromDec(code // base, base) + getS(code % base)
    return ""


print(fromDec(740, 2))


def toDec(code: str, base: int, i: int, j: int = 0):
    if i >= 0:
        return (getN(code[j])*(base**i)) + toDec(code, base, i-1, j+1)
    return 0
