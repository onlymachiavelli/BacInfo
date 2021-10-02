def readM():
    while(1):
        l = int(input("Enter L "))
        c = int(input("Enter C "))
        if(l in range(2, 11) and c in range(2, 11)):
            return {"l": l, "c": c}


def fillMatr(a: dict, li: list):
    for i in range(a["l"]):
        lin = []
        for j in range(a["c"]):
            while (1):
                ans = int(input(f"Enter this element of {i } {j} "))
                if(ans < 10 and ans >= 0):
                    break
            lin.append(ans)
        li.append(lin)


def Stick(matr: list, a: dict):
    res = []
    for i in range(a["l"]):
        string = ""
        for j in range(a["c"]):
            string += str(matr[i][j])
        res.append(string)
    return res


a = readM()
mat = []
fillMatr(a, mat)


print(Stick(mat, a))
