
from math import *
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


def form(x: int):
    return((2*x)/(2*x-1))*((2*x)/(2*x+1))


def wallis(ep: float):
    n = 3
    s = form(1)
    s1 = s*form(2)
    while (s1*2-s*2 > ep):
        s = s1
        s1 *= form(n)
        n += 1

    return (s1*2)


ep = 0.00000001

print(wallis(ep))
