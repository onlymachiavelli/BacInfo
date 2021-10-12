def size():
    while(1):
        n = int(input("Enter the size"))
        if n > 2:
            break


def fillFile(n):
    myFile = open("data.txt", "w")
    for i in range(n):
        myFile.write(input("Enter DATA")+"\n")
    myFile.close()


n = size()
fillFile(n)
