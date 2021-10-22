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

            
fin
"""
