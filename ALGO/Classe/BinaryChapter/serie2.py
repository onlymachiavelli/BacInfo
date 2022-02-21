
def getN(code: str):
    if not code.isnumeric():
        return ord(code) - 55
    return int(code)


def getS(code: int, base: int):
    if base < 16:
        return str(code)
    else:
        if code > 9:
            return chr(ord(str(code) + 55))
    return str(code)


def toDec(code: str, base: int, i: int = 0):
    if i >= 0:
        return (getN(code[i])*(base**len(code)-i-1)) + toDec(code, base, i-1)
    return 0


def fromDec(code: int, base: int):
    if code >= 0:
        return fromDec(code // base, base) + getS(code % base, base)
    return ""


def toBin(code: str):
    s = ""
    a = 0
    for i in range(len(code)):
        s += fromDec(toDec(code[i], 16), 2)
    return s


print(toBin("5D"))
