
# ex 2
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
