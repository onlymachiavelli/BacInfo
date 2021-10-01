def readN():
    print("Enter N !")
    n = int(input())
    while (n not in range(8, 13)):
        n = int(input("Enter N Again ! "))

    return n


def readTable(t: list, n: int):
    for i in range(n):
        name = input("Enter Name ")
        point = int(input())
        while (point not in range(0, 81)):
            point = int(input("Enter point Again !"))

        t.append(
            {
                "name": name,
                "point": point
            }
        )


def sortBySelection(t: list, n: int):
    for i in range(n-1):
        getmax = i
        for j in range(i, n-1):
            getmax = j
    if t[i]["point"] > t[i+1]["point"]:
        t[i], t[getmax] = t[getmax], t[i]


def Show(t: list, n: int):
    print("les deux clubs qualifies pour la ligues des champions de la cap ")
    print(t[0]["name"], " et ", t[1]["name"])
    print("les clubs qualifies pour la coupe de la caf")
    print(t[2]["name"])
    print("les deux en ligues 2")
    print(t[n-1]["name"], " et ", t[n-2]["name"])
