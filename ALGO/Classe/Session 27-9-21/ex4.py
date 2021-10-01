"""
ALGO :
Debut
    readKey(key)
    readChar(myChar)
    result <- getCrypt(Key, myChar)
    ecrire('YOUR RESULT IS ' , result )
Fin

TDO{
    reuslt = chaine
    key = entier
    myChar = chaine de charactere
}


proc readKey(@key:entier)
debut
    repeter
        ecrire("Enter the key")
    jusqu a key > 0

fin

proc readChar(@mychar:chaine )
debut

"""
# fill mat w condition ! ex


def fillMat(mat: list, w: int, h: int):

    for i in range(w):
        li = []
        for j in range(h):
            lin = int(input("Enter Ele !"))
            while lin > 9 or lin <= -10:
                lin = int(input("Enter Ele !"))
            li.append(lin)
        mat.append(li)
