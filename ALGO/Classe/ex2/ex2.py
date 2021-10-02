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
    mykey = input("Gimme the key step sis ! ")
    newkey = ""
    i = 0
    for j in range(len(char)):
        newkey += mykey[i]
        i += 1
        if (i == len(mykey)):
            i = 0

    return newkey


a = readchar()

print(readKey(a))
