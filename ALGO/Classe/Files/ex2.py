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
