def word():
    while(1):
        word = input("ENTER THE WORD ")
        if(word.isupper() and word.isalpha() and len(word) in range(3, 11)):
            return word


def fillMat(word: str, mat: list):
    apl = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

    newalpha = ""
    for wrd in word:
        if wrd == "W":
            newalpha += "V"
        else:
            newalpha += wrd
    for i in range(len(apl)):
        for alpha in newalpha:
            if apl[i] not in alpha:
                newalpha += apl[i]

    print(newalpha)


mymat = []

myword = word()


print(mymat)
fillMat(myword, mymat)
print(mymat)


""""
fonction isUpper(word:chaine):boolean
debut
    pour i de 1 a long(word):
        si word[i] non dans [A..Z] alors
            retourner faux
        fin si 
    retourner vrai
fin


fonction checkRepeat(word:chaine):boolean
debut 

    pour i de 1 a long(word)-1 faire
     pour j de i+1 a long(word)-1 faire 
        si word[i] = word[j] alors 
            retourner faux
        fin si

     fin pour
    fin pour
    retourner vrai

fin 


Fonction readWord():chaine de charactere
debut 


    
    tant que vrai faire 
        ecrire("Enter your word")
        lire(word)
        si (isUpper(word) et long(word) dans (3,13))et checkRepeat(word) alors
            retourner word 
        fin si
    fin tant que

fin

proc fillMat(mat:matrice, word):
debut
    alpha = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    line <- 0
    c <- 0
    ind = 1
    repeter
        mat[l][c] = word(ind)
        

        ind <- ind+1
        c <- c+1
        si c = 4 alors 
            c <- 0
            l <- l +1
        fin si
    jusqua ind = long(word)

fin




"""
