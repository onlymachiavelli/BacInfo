# LEFT RECT ALGORYTHM
import math


def f(x: float):
    # any function
    return math.cos(x) + math.ssqrt(x+1)


def leftRect(a: float, b: float, n: int):
    surf = 0
    x = a
    h = (b-a)/n
    for i in range(n):
        surf += f(x) * h
        x += h
    return surf


"""
fonction leftRect(a:reel, b:reel, n:entier) {
    debut 

        surf <- 0
        x <- a
        h <- (b-a)/n
        pour i de 1 a n faire {
            surf <- surf + f(x) *h

            find pour 
        }
        retourner surf

    find
}
"""

# RIGHT RECT ALGORYTHM


def rightRect(a: float, b: float, n: int):
    surf = 0
    h = (b-a)/n
    x = a + h
    for i in range(n):
        surf += f(x)*h
        x += h
    return surf


"""
fonction rightRect(a:reel, b:reel, n:entier) {
    debut

        surf <- 0
        h <- (b-a)/n
        x <- a + h
        pour i de 1 a n faire {
            surf <- surf + h*f(x)
            x <- x + h
        fin pour 
        }
        retourner surf
}
"""
# Middle Rect Algorythm


def midRect(a: float, b: float, n: int):
    surf = 0
    h = (b-a)/n
    x = a + h/2
    for i in range(n):
        surf += (x+h)*h
        x += h
    return surf


"""
fonction midRect(a:reel, b:reel, n:entier) {
    debut
        surf <- 0
        h <- (b-a)/n
        x <- a + h/2    
        pour i de 1 a n faire {
            surf <- surf + f(x)*h
            x <- x + h
        fin pour
        
        }
        retourner surf
    find
}

"""

# TRAPEZOID ALGORYTHM


def trapSurf(a: float, b: float, n: int):
    h = (b-a)/n
    x = a+h/2
    s = 0
    for i in range(n):
        s += (f(x) + f(x+h))*(h/2)
        x += h
    return s


"""
fonction trapSurf(a:reel, b:reel, n:entier) {
    debut
        h <- (b-a)/n
        surf <-0
        x <- a + h/2
        pour i de 1 a n faire {
            surf <- surf + (f(x) + f(x+h))*(h/2)
            x <- x + h
        fin pour
        }
        retourner surf
    fin 
    }
"""
