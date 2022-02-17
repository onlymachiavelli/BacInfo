

import encodings


def enCoding(code: int, mode: int):
    if code >= mode/2:
        return enCoding(code//mode, mode) + str(code % mode)
    return ""


print(enCoding(860, 2))
