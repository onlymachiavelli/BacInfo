def Size():
    while(1):
        n = int(input("Enter the size"))
        if n > 2:
            return n


def fillFile(n: int):
    myFile = open("data.txt", "w")
    for i in range(n):
        ans = input("Enter Data ")
        myFile.write(f"{ans}\n")
    myFile.close()


def fillArr(t: list, n: int):
    myFile = open("data.txt", "r")
    lines = myFile.readlines()
    counter = 0
    for line in lines:
        sym = line[0] == line[len(line)-1]
        voy = line[0].upper() in "AEIOUY"
        counter += 1
        t.append({
            "num": counter,
            "sym": sym,
            "voy": voy
        })
    myFile.close()


def FillFilet(t: list, n):
    myFile = open("result.txt", "w")
    for i in range(n):
        myFile.write(f"Ligne {t[i]['num']} {t[i]['sym']} {t[i]['voy']}")
    myFile.close()


n = Size()
fillFile(n)
