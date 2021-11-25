

def bub(n, mat, p):
    check = False
    while not check:
        check = True
        for i in range(n-1):
            if (mat[p][i] > mat[p][i+1]):
                mat[p][i], mat[p][i+1] = mat[p][i+1], mat[p][i]
                check = False


def sortmat(mat, n):
    for i in range(n):
        bub(n, mat, i)


mat = [
    [0, 5, 6, 9],
    [3, 9, 6, 4],
    [10, 50, 68, 89],
    [8, 0, 30, 80]
]
#n = len(mat)
#sortmat(mat, n)
# print(mat)


while True:

    code = input()

    quit = False
    i = len(code)
    ch = ""
    while not quit:
        i -= 1
        if (code[i].isnumeric()):
            ch = code[i] + ch
        else:
            quit = True
    if (len(code) >= 6 and code.find("TU") != -1 and len(ch) > 0):
        break
ch = str(int(ch) + 1)
print(code[0:i+1] + ch)


"""
Algo 
debut 

    repeter
        ecrire("enter the code")
        lire(code)
        quit <- faux
        i = <- long(code)
        ch <- ""
        tant que quit = faux faire :
            i <- i - 1
            si estnum(code[i]) alors 
                ch <- code[i] + ch
            sinon 
                quit <- vrai
            fin si 
        fin tant que 

    jusqua long(code) >= 6 et pos(Majus(code),"TU") != -1 et long(ch) != 0

    ch <- convch(valeur(ch)+1)

    ecrire(code[0,i]+ch)





fin
"""
