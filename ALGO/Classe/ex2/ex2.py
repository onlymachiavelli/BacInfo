"CODE DE GRONSFELD"


def readchar():
    while(1):
        ch = input("Enter your character ")
        check = 0
        for i in range(len(ch)):
            if (ch[i].isupper() and ch[i].isalpha()):
                check += 1
        if check == len(ch):
            return ch


def readKey(char: str):
    # just a controller
    while (1):
        i = 0
        mykey = input("Gimme the key step sis !")
        for j in range(len(mykey)):
            if mykey[j].isalnum():
                i += 1
        if i == len(mykey):
            break
    newkey = ""
    i = 0
    for i in range(char):
        newkey += newkey[i]
        i += 1
        if (i == len(mykey)):
            i = 0

    return newkey


a = readchar()

b = readKey(a)
print(b)
