"""

TDNT{
    Eval = enregistrement 
        nom : chaine 
        num : entier
        oper : chaine
        rep : entier
    
    fin enregistrement

    fiche : fichier de type Eval
}


--module programme pricipale : 
Algorithme Progshit
debut
    FillHiseb(fh)
    n <- 0
    FillEve(n, fh, fe)
    GenStat(n, fs, fe)
fin
----------------------
TDO{
    n : entier
    fh : texte
    fe : fichier de tab
    fs : texte

}

--module FillHis
procdedure FillHis(@fh):
debut
    ouvrir ("C:\Hizeb.txt", fh, "w")
    pour i de 1 a 10 faire
        repeter 
            ecrire("Enter equation")
            lire(eq)
        jusuqua verfEq(eq)
        ecrire_ln(fh, eq)
    fin pour

fin
TDOL {
    i : entier
    eq: chaine
    verfEq : fonction 
}


--module verf 
fonction verfEq(mySTring : chaine) : booleen 
debut 
        si pos("+" , myString) = -1 alors
            retourner faux
        fin si
    pour i de 0 a long(myString)-1 faire
        
        si myString[i] ∉ ["0", "9"] et myString[i] != "+" alors 
            retourner faux 
        fin si 
    fin pour 
        
    si myString[0] = "+" ou myString[long(myString) - 1] = "+" ou pos("++", myString) != -1 alors 
            retourner faux
        fin si

    retourner vrai
fin 

TDOL{
    i : entier
}

module fillelev

procedure FillEle (@n:entier, @fh : texte, @fe: fiche)
debut 
    
    ouvrir("C:\Elev.dat", fe, "wb")
    quit <- false 
    tant que quit = faux faire 
        ouvrir ("C:\Hizeb.txt", fh, "r")
        repeter 
            ecrire("enter your name ")
            lire(eve.nom)
        jusqua 4<= long(eve.nom) <= 15

        repeter 
            ecrire("op num")
            lire(eve.num)
        jusqua 1 <= eve.num <= 10

        pour i de 1 a eve.num faire 
            lire_ligne(fh, eve.opr)
        fin pour 
        
        ecrire("give rep")
        lire(eve.rep)
        fermer(fh)

        ecrire("Do you want to add another competito ? y if yes or another shit if no ")
        lire(ans)
        si (majus(ans) = "Y" ) alors 
            quit <- false 
        sinon 
            quit <- vrai
        
        ecrire(fe, eve)
        n <- n+1
    fin tant que 

fin




TDOl :{
    i :entier
    eve : Eval 
    quit : booleen 
    ans : char
}


module gen stat 
procedure GenStat(n: entier, @fe:fiche, @fs:text)

debut 
    ouvrir("C:\Elev.dat", fe, "rb")
    ouvrir("C:\stat.txt", fs, "w")
    total <- 0
    pour i de 1 a n faire 
        lire(fe ,eve)
        si Check(eve.opr, eve.rep) alors 
            total <- total + 1
            ecrire_ln(fs, eve.nom)
        fin si 
        ecrire_ln(fs, convch(total *100 div n))
    fin pour 
    fermer(fs)
    fermer(fe)
fin

tdol{
    i : entier 
    total : entier 
    eve : Eval 
    Check : fonction
}

module verf somme 
fonction Check (myString : chaine, num : entier) : booleen 
debut   
    sum <- 0
    cnum <- ""
    pour i de 0 a long(myString) faire 
        si myString[i] != "+"
            cnum <- cnum + myString[i]
        sinon 
            sum <- sum + conventier(cnum)
            cnum <- ""
        fin si 
    fin pour  
    retourner sum = num
fin 

TDOL {
    sum : entier 
    cnum :chaine 
    i : entier 

}
"""


import pickle


def verfEq(myString):
    if (myString.find("+") == -1):
        return False
    for i in range(len(myString)):
        if (not (0 <= int(myString[i]) <= 9) and myString[i] != "+"):
            return False
    if myString[0] == "+" or myString[len(myString) - 1] == "+" or myString.find("++") != -1:
        return False
    return True


def FillHis():
    fh = open("hizeb.txt", "w")
    for i in range(10):
        check = False
        while not check:
            print("Enter equation")
            eq = input()
            check = verfEq(eq)
        fh.write(eq+"\n")


def FillEle():
    fe = open("elev.dat", "wb")
    quit = False
    while not quit:
        fh = open("hizeb.txt", "r")
        q = False
        while not q:
            print("Enter your name")
            nom = input()

            q = 4 <= len(nom) <= 15
