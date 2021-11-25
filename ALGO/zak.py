"""
TDONT{
    mat : tableau 9*9 entier
}

Algo bachmanity
Debut
    n <- alea(3, 9)
    fillMat(n,m)
    src <- "c:\bach.txt"
    genFile(n, m, src)

Fin

TDO{
    n : entier
    src : chaine 
    m : mat 
    fillMat, genFile  : procedure 

}

procedure fillMat(n : entier, @m:mat):
DEBUT
    pour i de 0 a n-1 faire
        pour j de 0 a n-1 faire 
            m[i,j] <- alea(1,9)
        fin pour 
    fin pour 

FIN

TDOL{
    i : entier
    j : entier

}

procedure genFile(n:entier,m:mat, src: chaine )
debut 
    ouvrir(src,fs, "w")
    b_total <- 0 
    pour i de 0 a n-1 faire 
        somme <- 0
        pour j de 0 a n-1 faire 
            somme <- somme + m[i,j]
        fin pour 
        b_total <- b_tootal + somme
        ecrire_nl(fs, "Ligne "+ i+1 + convch(somme))
    fin pour 
    ecrire_nl("Total : " + convch(b_total))
    fermer(fs)

fin
TDOL{
    i,j,somme, b_total : entier
    fs : texte 


} 
"""
