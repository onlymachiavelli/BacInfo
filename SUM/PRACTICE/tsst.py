"""from math import *


def f(x):
    return cos(x) + sqrt(x+1)


def trap(n, a, b):
    h = (b-a)/n
    s = 0
    x = a
    for i in range(n):
        s += (f(x) + f(x+h)) * (h/2)
        x += h

    return s


print(trap(50000, 1, 3))


2.74736427
2.747345383452616
2.747364273500522"""


def powe(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res


print(powe(6, 3))
