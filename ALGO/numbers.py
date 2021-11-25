

def isPrime(n, i=2):
    if n // 2 > n:
        return False
    if n % i == 0:
        return True
    return isPrime(n, i + 1)


print(isPrime(4))
