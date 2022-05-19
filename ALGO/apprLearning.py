def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n-1)


def power (x: float, n: int) -> float:
    if n == 0:
        return 1
    return x * power(x, n-1)


def sinus(x:float, ep:float) -> float :
    one = 1 
    n = 1 
    s1 = power(x,1) / fact(1) * one 
    
    one *= -1 
    n+=2 
    s2 = s1 + (power(x,n) / fact(n)) * one 
    one *= -1
    while abs(s1 - s2) >= ep:
        s1 = s2
        n+=2
        s2 = s1 + (power(x,n) / fact(n))*one
        one *= -1
    return s2

print(sinus(1, 0.0000000001))