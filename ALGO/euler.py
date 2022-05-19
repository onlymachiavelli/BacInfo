def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n-1)



def euler() -> int:
    n=0
    s1 = 1/fact(n)
    n+=1
    s2 = s1 + 1/fact(n)
    while abs(s1 - s2) >= 0.0000000001:
        s1 = s2
        n+=1
        s2 = s1 + 1/fact(n)
    return s2

print(euler())