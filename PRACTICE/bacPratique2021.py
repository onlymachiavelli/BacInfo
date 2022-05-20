import numpy as np


def arrLen(src: str):
    myFile = open(src, "r")
    n = 0
    while (myFile.readline()):
        n += 1
    myFile.close()
    return n


def hexaTodecimal(code: str):
    if len(code) > 0:
        if code[0].isnumeric():
            return (int(code[0])) * (16 ** len(code)-1) + hexaTodecimal(code[1:])
        else:
            return int(ord(code[0]) - 55) * 16 ** len(code)-1 + hexaTodecimal(code[1:])

    else:
        return 0


# PP
src = "imgHexa.txt"
fileLen = arrLen(src)
matrix = np.zeros(fileLen, dtype=object)


print(hexaTodecimal("41"))
