

def isPrime(n, i=2):
    if n // 2 > i:
        return True
    if n < 2 or n % i == 0:
        return False
    return isPrime(n, i + 1)


#print([isPrime(x) for x in [1, 9, 20]])


def tri(n, t):
    change = True
    while change:
        change = False
        for i in range(n-1):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
                change = True


t = [0, 8, 6, 7, 4, 3]
n = len(t)
tri(n, t)
print(t)
