import math


def readN():

    print("Enter N !")
    n = int(input())
    while(n not in range(2, 21)):
        print("Enter N again")
        n = int(input())
    return n


def fillArr(li: list, n: int):
    a = 0
    b = 0
    for i in range(n):
        a = int(input(" Give A "))
        b = int(input(" Give B "))
        li.append({
            "a": a,
            "b": b
        })


def showArr(li: list, n: int):
    for i in range(n):
        print(li[i])


def fillArrM(marr: list, li: list, n: int):
    for i in range(n):
        marr.append(math.sqrt((li[i]["a"] ** 2) + (li[i]["b"] ** 2)))


def Sorting(li: list, mis: list, n: int):
    for i in range(n-1):
        if mis[i] < mis[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
            mis[i], mis[i+1] = mis[i+1], mis[i]
            Sorting(li, mis, n)


def showT(mist: list, n: int):
    for i in range(n):
        # print(f"{int(mist[i]['a'])}+{int(mist[i]['b'])}i")
        return 0


l = []
m = []
n = readN()


fillArr(l, n)
fillArrM(m, l, n)
Sorting(l, m, n)
print("List ")
showArr(l, n)
print("Mist")
showArr(m, n)
showT(m, n)
