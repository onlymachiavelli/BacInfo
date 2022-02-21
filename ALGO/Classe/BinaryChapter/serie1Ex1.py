def check(myString: str):
    fuck = True
    for i in range(len(myString)):
        if myString[i] != "0" and myString[i] != "1":
            fuck = False
    return fuck


def fillBin():
    myString = str(input("Enter your binary Code ! : "))
    if check(myString):
        return myString
    return fillBin()


def toDec(code: str, base: int, i: int, j: int = 0):
    if i >= 0:
        return (int(code[j]))*(base**i) + toDec(code, base, i-1, j+1)
    return 0


def splitShit(myString: str):
    loc = myString
    h = ""
    while len(loc) % 4 != 0:
        loc = "0" + loc
    print(loc)
    while len(loc) > 0:
        x = toDec(loc[0:4], 2, 3)
        if x <= 9:
            c = str(x)
        else:
            c = chr(x + 55)
        h += c
        loc = loc[4:len(loc)]
    print(h)


myString = fillBin()
splitShit(myString)
