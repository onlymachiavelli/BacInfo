from os import read


def readN():
    print("Enter N !")
    n = int(input())
    while (n not in range(5, 21)):
        print("Enter N correct !")
        n = int(input())
    return n


def fillT(n: int, t: list):
    for i in range(n):
        print("Enter Matr")
        t[i]["matr"] = int(input())
        name = input("Enter Name ")
        lname = input(" Ente Lname 5")
        t[i]["nopm"] = f"{name} {lname}"
        while(1):
            dc1 = float(input())
            dc2 = float(input())
            ds = float(input())
            if(dc1 and dc2 and ds in range(0, 21)):
                break
        t[i]["eval"]["dc1"] = dc1
        t[i]["eval"]["dc2"] = dc2
        t[i]["eval"]["ds"] = ds


n = readN()

t = [
    {
        "matr": 0,
        "nopm": "",
        "eval": {}
    }
] * n
fillT(n, t)
print(t)
