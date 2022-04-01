
# ex 2
from cmath import sqrt


def febApp(ep: float):
    a = 1
    b = 1
    vz = b/a
    u = a+b
    a = b
    b = u
    v1 = b/a
    while abs(v1 - vz) > ep:
        vz = v1
        u = a+b
        a = b
        b = u
        v1 = b/a
    return v1


ep = 0.0000000001
print(febApp(ep))
print()
# ex 3


def prime(n: any):
    return 0


def brun(ep: float):
    s1 = 0
    i = 3
    while True:
        s = s1
        if prime(i) and prime(i+2):
            s1 = s + 1/i + 1/i+2
        i += 2
        if abs(s1-s) <= ep:
            break
    return s1


# p
# A
# n
# formule arrangement  n!/((n-p)!) ordonnee

# comb :

# p
# C
# n
# formule combinaison : A(n...p) / p! non ordonnee


# permetation : n!


# ex 4
def comb(n: int, p: int):

    return 0


# ex 5  gauche
def ex5(a, b, n):
    h = (b-a)/n
    x = a
    s = 0
    for i in range(1, n):
        s += 1/sqrt(x)
        x += h
    return h * s
# droite


def ex5(a, b, n):
    h = (b-a)/n
    x = a + b
    s = 0
    for i in range(1, n):
        s += 1/sqrt(x)
        x += h
    return h * s
# trapez


def tra(a, b, n):
    h = (b-a)/n
    x = a
    s = 0
    for i in range(1, n):
        s += 1/sqrt(x) + 1/sqrt(x+h)
        x += h
    return h * s
# willis trapez willis rectangle (droite gauche milieu )
