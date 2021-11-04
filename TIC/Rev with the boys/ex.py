"""
Algo PP
debut
    n <- 0
    fillCommande(n, fc)
    bill(n, fc, ft)
    show(n, ft)

fin


TDNT : 
    article = enregistrement 
        nom : chaine
        qte : entier
        prix : reel
        etat : booleen
    data : tableau 100 article
TDO :
     n : entier
     fillCommande : procedure
     bill : procedure
     show(procedure)
     fc : article 

     
procedure fillCommande(@n : entier, @fc: data)
debut 
    ouvrir("C:\commande.dat", fc, "wb")
    check <- faux
    tant que check = faux faire
        ecrire("Add element ? y if yes or other if no")
        lire (ans)
        si majus(ans) = "Y" alors 
            ecrire(")
            lire(t[n].nom)
            ecrire("QTE ")
            lire(t[n].qte)
            ecrire("price")
            lire(t[n].prix)
            ecrire("etat")
            lire(t[n].etat)
            n += 1

        sinon 
            check = vrai
    fin tant que
    ecrire(fc, t)
    fermer(fc)
fin 
TDOL
    t : data
    ans : caractere
    check : booleen





procedure Bill(n : entier, @fc:data, ft:texte)
debut 
    ouvrir("C:\data.dat", fc, "rb")
    ouvrir("C:\facture.txt", ft, "w")
    lire(fc,ar)
    total <- 0
    pour i de 0 a n-1 faire 
        ecrire_ln(ft, ar[i].nom + convch(ar[i].prix *ar[i].qte))
        total <- total +ar[i].prix * ar[i].qte
    fin pour
    ecrire_ln(ft, convch(total))
    fermer(fc)
    fermer(ft)
fin 

TDOL 
    ar : data
    i : entier
    total : entier
"""


import pickle


def fillCommande():
    global n
    fc = open("commande.dat", "wb")
    check = False
    t = []
    while not check:
        print("Add element  ? ")
        ans = input()
        if(ans.upper() == "Y"):
            name = input("Enter name ")
            qte = int(input("Enter QTE"))
            price = float(input("Enter price "))
            etat = bool(input("Enter State"))
            t.append({
                "nom": name,
                "qte": qte,
                "prix": price,
                "etat": etat
            })
            n += 1
        else:
            check = True

    pickle.dump(t, fc)
    fc.close()


def Bill(n: int):
    fc = open("commande.dat", "rb")
    ft = open("facture.txt", "w")
    ar = pickle.load(fc)
    total = 0
    for i in range(n):
        ft.write(f"{ar[i]['nom']} {int(ar[i]['qte'] * ar[i]['prix'])} \n")
        total += ar[i]['qte'] * ar[i]['prix']
    ft.write(str(int(total)))
    fc.close()
    ft.close()


# PROG PRINC
n = 0
fillCommande()
Bill(n)
