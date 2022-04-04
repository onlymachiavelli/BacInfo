import math


def f(x: float):
    return math.sqrt(1-x**2)


def milieu(n: int):
    h = 1/n
    x = h/2
    s = 0
    for i in range(n):
        s += f(x)
    return s


def val():
    global ep
    s0 = milieu(1)
    s1 = milieu(2)
    n = 2
    while abs(4*s1 - 4*s2) > ep:
        s0 = s1
        s1 = milieu(n)
        n += 1


def val2():
    s1 = (16/5) - (4/239)
    i = 3

    quit = False
    while not quit:
        s0 = s1


ep = 0.0001
