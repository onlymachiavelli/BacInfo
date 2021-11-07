
"""


Algo hhh
debut 
n <- size()
fill(fp, n)
genfr(fr, fp, n)
fin


TDONT{
    pride = enregistrement 
        codp : chaine
        des : chaine 
        ean13 : chaine 
    fin enregistrement 
    fiche : fichier de type pride


}


TDO{
    n:entier
    fp : fiche 
    fr : texte 
    fill, genfr : proc
    size : fonction 

}



module size 
fonction size() : entier
debut 
    repeter
        ecrire("med asba n")
        lire(n)
    jusqua 10 <= n <= 50
    retourner n

fin 




module verifier codeqr

fonction Test(code:chaine):boleen
debut
    si long(code) != 13 alors 
        retourner faux
    fin si
    cc <- code[long(code)-1]
    s <- 0
    q <- ""
    pour i de 0 a 11 faire
        q <- q + code[i]
    fin pour 

    pour i de 0 a 11 faire  
        si (i mod 2 == 0) alors 
            s <- s + conventier(q[i])
        sinon 
            s <- s + ent(q[i]) * 3
        fin si 
    fin pour 
    
    r <- s mod 10
    retourner 10-r = cc

    

fin
module zarafa
procedure fill(@fp : fiche, n:entier):
debut
    ouvrir("C:\XNXX.DAT", fr, "wb")
    pour i de 1 a n faire 
        repeter 
            ecrire("med nayek code p ")
            lire(gay.codp)
        jusqua isNum(gay.codp) et long(gay.codp) = 6

        repeter 
            ecrire("med nayek des")
            lire(gay.des)
        jusqua 1 <= long(gay.des) <= 20
        repeter 
            ecrire("zabour ommek ean13")
            lire(gay.ean13)
        jusuqua Test(gay.ean13)

        ecrire(fp, gay)
    fin pour
    fermer(fp)
fin



fonction isNum(str: chaine):booleen
debut 
    pour i de 0 a long(str) -1 faire
        si 0<=ent(str[i])  <= 9 = faux alors 
            retourner faux 
        fin si 

        retourner vrai 
fin

tdol{
    i :
}



procedure gen (@fr:text, @fp:fiche, n:entier)
debut 
    ouvrir("C:\xnxx.dat", fp, "rb")
    ouvrir("c:pornhub.txt", fr, "w")

    ecrireln("nombre totale des produits="+convch(n))
    ch <- ""
    lire(fp, gay)
    pour i de 1 a n faire 
        ch<- ch + gay.codp + " "
    fin pour 
    ecrire_ln(fr,ch)
    ch = ""
    pour i de 1 a n faire 
        si (Test(gay.ean13) = faux) alors 
            ch <- ch+ gay.ean13 + " " 
        fin si
    fin pour

    ecrire(fr, "zeb zeb " + ch)


fin 



ligne 2 : codp 










"""
