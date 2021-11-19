"""
Algorythm ex {
    Debut
        saisir(n)
        src <- "source.txt"
        remplir (src, n)
        genererM(src, n, m)
        triN(m,n)
        src1 <- "source1.txt"
        generer(src , m, n)
        
    Fin
}

"""


def saisir():
    global n
    quit = False
    while not quit:
        n = int(input("Enter n "))
        quit = n in range(3, 16)


def remplirS(n, src):
    f = open(src, "w")
    for i in range(n):
        quit = False
        while not quit:
            lg = input("Enter Number structure ")
            quit = lg.isnumeric()
        f.write(lg+"\n")


# PP
n = 0
saisir()
src0 = "source0.txt"

remplirS(n, src0)
