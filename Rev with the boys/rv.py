"""
{
    Saisir texte eq
    Remplir eleve
    Static
}



algo 
debut
eq(fe)
n <- 0
Elev(fe,fee,n)
fin 



module verification 

fonction verif(myString: chaine) : booleen
debut
    si pos("+", myString) = -1 alors 
        retourner faux
    fin si 

    pour i de 0 a long(myString)-1 alors 
        si myString[i] !E ["0", "9"] alors 
            retourner faux 
        fin si 
    fin pour 
    si myString[0] = "+" ou myString[long(myString)-1] = "+" ou pos("++", myString) != -1 alors
        retourner faux
    fin si 
    retourner vrai
fin


Module Remplir Texte Eq
procedure eq(@fe):
debut
    ouvrir("c:\xnxx.txt", fe, "w")
    pour i de 1 a 10 faire 
        repeter
            ecrire("Donner eq")
            lire(eq)
        jusqua verif(eq)
    fin pour
    fermer(fe)

fin
TDOL{
    i : entier
    verif: fonction
    eq : chaine
}

TDONT{
    elev  = enregistrement 
        nom  : chaine 
        num : entier 
        opr : chaine 
        rep : entier
    fin

    fiche  : fichier de type elev 
}

module remplir eleve 
procedure Elev(@fee, @n):
debut
    ouvrir("c:\elev.dat",fee, "wb")
    quit <- faux
    tant que quit = faux faire
        ouvrir("c:\xnxx.txt", fe, "r")

        n <- n + 1
        repeter 
            ecrire("entrer nom")
            lire(gay.nom)
        jusqua long(gay.nom) >= 3

        repeter 
            ecrire("med nayek num")
            lire(gay.num)
        jusqua 1 <= gay.num <= 10

        pour i de 1 a gay.num faire 
            lire_ln(fe, gay.opr)
        fin pour
        
        ecrire("med nayek rep")
        lire(gay.rep)


        ecrire(fee, gay)
        fermer(fe)  
        ecrire("theb asba tzid eleve ekher? y ken oui snn ay haja okhra ken le ")

        lire(ans)
        si majus(ans) != "Y" ou majust(ans) != "YES" alors 
            quit = True
        fin si
    fin tant que
            
    
fin


tdo { 
    fe : 
}
"""


myfile = open("sex.dat", "rb")

a = []

quit = False


fermer(mahrez)
