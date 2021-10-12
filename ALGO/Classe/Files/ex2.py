def Size():
    while(1):
        n = int(input("Enter the size "))
        if n in range(2, 16):
            return n


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
