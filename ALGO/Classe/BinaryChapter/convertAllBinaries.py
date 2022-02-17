def fromDec(code: int, base: int):
    if code > 0:
        return fromDec(code // base, base) + str(code % base)
    return ""


print(fromDec(740, 2))
