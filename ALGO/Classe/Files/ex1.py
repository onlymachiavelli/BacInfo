def Size():
    while(1):
        n = int(input("Enter the size"))
        if n > 2:
            return n


def fillFile(n: int):
    myFile = open("data.txt", "w")
    for i in range(n):
        myFile.write(input("Enter DATA")+"\n")
    myFile.close()


n = Size()
fillFile(n)
