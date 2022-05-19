from math import *

def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n-1)



def euler() -> float:
    n=0
    s1 = 1/fact(n)
    n+=1
    s2 = s1 + 1/fact(n)
    while abs(s1 - s2) >= 0.0000000001:
        s1 = s2
        n+=1
        s2 = s1 + 1/fact(n)
    return s2

def power (x: float, n: int) -> float:
    if n == 0:
        return 1
    return x * power(x, n-1)


def eulerPIusingFact(ep:float) -> float :
    n=1 
    s1 = (1/fact(n))
    n+=1 
    s2 = s1 + (1/fact(n))
    while abs(s1*6 - s2*6) >= ep:
        s1 = s2
        n+=1
        s2 = s1 + (1/fact(n))
    return sqrt(s2*6)
def eulerPI(ep:float) -> float  :
    n=1 
    s1 = 1/power(n, 2) 
    n+=1 
    s2 =s1 + 1/power(n, 2)
    while abs(s2-s1) >= ep :
        s1 = s2
        n+=1
        s2 = s1 + 1/power(n,2)
    return sqrt(s2*6)


print(eulerPI(0.00000001))