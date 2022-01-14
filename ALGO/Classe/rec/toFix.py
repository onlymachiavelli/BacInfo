from math import sqrt


def saisirN():
    n = int(input("give n : "))
    if 4000 < n < 10000:
        return n
    else:
        return saisirN()


def isPrime(n: int, i: int = 2):
    if n > 1:
        if i > sqrt(n):
            return True
        return n % i != 0 and isPrime(n, i+1)
    else:
        return False


def super_prime(n):
    if n == 0:
        return True
    else:
        if isPrime(n, 2) == False:
            return False
        else:
            return super_prime(n // 10)


n = saisirN()
print(n)
for i in range(1, n+1):
    if isPrime(i):
        print(i)
        print(super_prime(i))
