"""
ALGO : pol
debut
    n <- size()
    fillMat(n,@mat)
    fillFile(n,mat,@f)
fin


TDO : 
    n : entier
    mat : matrice
    f:texte
    size : fonction
    fillMat : procedure
    fillFile: procedure
TDNT:
    matrice : tableau 15*15 caractere
----------------------

fonction size():entier 
debut 
    repeter 
        ecrire("Enter N")
        lire (n)
    jusqua 2 <= n <= 15
    retourner n
fin 

TDOL : 
    n : entier


procedure fillMat(n:entier, @mat:matrice)
debut 

    pour i de 0 a n-1 faire
        pour j de 0 a n-1 faire
            repeter 
                ecrire("Enter",i,j)
                lire(mat[i,j])
            jusqua "A" <=mat[i,j] <= "Z"
        fin pour
    fin pour

fin
TDOL:
    i : entier
    j : entier


fonction isPal(string:chaine):booleen
debut
    rev<-""
    i <- long(string)
    tant que i != 0 faire
        i <- i-1
        rev <- rev + string[i]
    fin tant que
    retourner rev = string

fin


procedure fillFile(n:entier, m:matrice, @f)
debut 
    ouvrir("c:\bac22\sym.txt", f, "w")
    nbc = =
    nbl = 0
    chl = "*"
    chc = "*"
    pour i de 0 a n-1 faire 
        ch1 = ""
        ch2  = ""
        pour j de 0 a n-1 faire
            ch1 <- ch1 + m[i,j]
            ch2 <- ch2 + m[j,i]
        fin pour
        si isPal(ch1) alors 
            chc <- chc + ch1
            nbc <- nbc + 1
        fin si
        si isPal(ch2) alors 
            chl <- chl + ch2
            nbl <- nbl + 1
        fin si
    fin pour 
    effacer(chl, chl[long(chl)-1])
    effacer(chc, chc[long(chc)-1])
    ecrireln(f, chc)
    ecrireln(f, nbc)
    ecrireln(f, chl)
    ecrireln(f, nbl)
fin


TDOL:
    i,j,nbc,nbl:entier
    ch1,ch2,chl,chc:chaine


"""


def size():
    while(1):
        print("enter n")
        n = int(input())
        if n in range(2, 16):
            return n


def fillMat(n: int, mat: list):
    for i in range(n):
        for j in range(n):
            check = False
            while (not check):
                print(f"enter caracter of {i, j}")
                mat[i][j] = input()
                check = "A" <= mat[i][j] <= "Z" and len(mat[i][j]) == 1


def isPal(string):
    i = len(string)
    ch2 = ""
    while (i >= 0):
        i -= 1
        ch2 += string[i]
    return ch2 == string


def fillFile(n: int, m: list):
    myFile = open("sym.txt", "w")
    chl = "*"
    chc = "*"
    nbc = 0
    nbl = 0
    for i in range(n):
        ch1 = ""
        ch2 = ""
        for j in range(n):
            ch1 = m[i][j]
            ch2 = m[j][i]
        if (isPal(ch1)):
            chc += ch1
            nbc += 1
        if isPal(ch2):
            nbl += 1
            chl += ch2
    chl = chl[:len(chl)-2]
    chc = chc[:len(chc)-2]
    myFile.write(chl+"\n" + str(nbl) + "\n" + chc + "\c" + nbc)


n = size()
mat = [[""*n]*n]
fillMat(n, mat)
fillFile(n, mat)
