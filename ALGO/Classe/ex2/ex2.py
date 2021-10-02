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


def conv(key: str, char: str):
    crpt = ""
    for i in range(len(char)):
        od = ord(char[i]) + int(key[i])
        if(od > 90):
            od -= 26
        crpt += chr(od)
    return crpt


a = readchar()

mykey = readKey(a)
res = conv(mykey, a)
print(res)
