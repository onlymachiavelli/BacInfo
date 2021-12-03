"""
Algorithme devoir 
debut 
    src <- "asba.txt"
    src2 <- "zebAlaa.txt"
    n <- size(src)
    remplirmat(n,m,src)
    gentxt(n,m,src2)
    fillBinary(n, m ,"dick.bat")

fin
TDO{
    src, src2 : chaine 
    n : entier
    m : mahrez
    remplirmat, gentxt : procedure
    size : fonction 

}
TDONT{
    mahrez : tableau de 100 * 100 entier
    cord = enregistrement 
        i: entier
        j: entier
    fin 

    mymax = enregistrement 
        themax : entier
        cordo : cord 
    fin 

    fiche : fichier binaire de type mymax



}
fonction size (src: chaine ): entier 
debut 
    ouvrir(src, alaa, "r")
    n <- 0
    repeter
        lire_ligne(alaa, ch)
        n <- n + 1
    jusqua fin_fichier(alaa)
    retourner n
fin
TDOL{
    alaa : texte 
    n : entier
    ch : chaine
}

procedure fillmat(n:entier, @m : mahrez , src: chaine)
debut 
    ouvrir(src, qahba, "r")
    num <- ""
    pour i de 0 a n-1 faire 
        lire_ligne(qahba, ch)
        pour j de 0 a long(ch)-1 faire 
            si(estnum(ch[i])) alors 
                num <- num + ch[i]
            fin si 
        fin pour 
        tant que long(num) < n alors 
            num <- num + convch(alea(0,9))
        fin tant que 
        pour k de 0 a n-1 faire 
            m[i,k] <- valeur(num[k])
        fin pour 
    fin pour 

    fermer(qahba)
Fin

TDOL{
    i,j,k : enttier
    num : chaine
    ch : chaine 
    qahba : texte
}



procedure gentxt(n:entier, m:mahrez, src2:chaine)
debut
    ouvrir(src2, abla, "w")
    all <- 0
    pour i de 0 a n-1 faire 
        sum <- 0
        pour j de 0 a n-1 faire 
            sum <- sum + m[i,j]
        fin pour 
        all <- all + sum
        ecrire_nl(abla, "Somme de Ligne " + convch(i+1) + " est : " +  convch(sum))
    fin pour 
    ecrire_nl(abla, "Total : " + convch(all))

    fermer(abla)
Fin


TDOL{
    all : entier
    sum : entier
    i : entier 
    j : entier
    abla : text 

}

procedure fillBinary(n: entier, m: mahrez, src3:chaine)
debut 
    ouvrir(src3, mybin, "wb")
    pour i de 0 a n-1 faire 
        myj <- 0
        mx <- m[i,0]
        pour j de 0 a n-1 faire
            si themax < m[i,j] alors
                themax <- m[i,j]
                myj <- j
            fin si
        fin pour 
        a.themax <- mx
        a.cordo.i <- i
        a.cordo.j <- myj
        ecrire(mybin, a)
    fin pour 
    fermer(mybin)   
fin

"""
