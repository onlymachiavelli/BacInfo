import math
# a, b N


def f(x: float):
    return math.cos(x) + math.sqrt(x)


def leftRect(a: float, b: float, n: int):
    x = a
    h = (b-a)/n
    s = 0
    for i in range(n):
        s += f(x) * h
        x += h
    return s


def rightRect(a: float, b: float, n: int):
    h = (b-a)/n
    x = a+h
    s = 0
    for i in range(n):
        s += f(x+h) * h
        x += h
    return s


def middRect(a: float, b: float, n: int):
    h = (b-a)/n
    x = a+h/2
    s = 0
    for i in range(n):
        s += f(x) * h
        x += h
    return s


def trap(a: float, b: float, n: int):
    h = (b-a)/n
    x = a+h/2
    s = 0
    for i in range(n):
        s += (f(x) + f(x+h))*(h/2)
        x += h
    return s
