from math import sqrt

ep = 0.00000000001


def apprx(e: float):

    n = 2
    s1 = 1
    s = s1+(1/(n**2))
    while abs(sqrt(6*s1) - sqrt(6*s)) > e:
        s1 = s
        s = s1+(1/(n**2))
        n += 1
    return sqrt(6*s)

# middle PT


def surf(a, b, n):
    s = 0
    h = (b-a)/n
    for i in range(n):
        s += h*(a+i*h+h/2)
    return s
