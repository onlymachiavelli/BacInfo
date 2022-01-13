from math import sqrt
from pickle import *


def size():
    n = int(input("Enter n "))
    if 40000 < n < 100000:
        return n
    else:
        return size()


def isPrime(n: int, i: int = 2):
    if n > 1:
        if i > sqrt(n):
            return True
        return n % i != 0 and isPrime(n, i+1)
    else:
        return False


def isSuperPrime(n: int, i: int):
    if i >= 1:
        print(i)
        print(isPrime(i))
        return isPrime(i) and isSuperPrime(n, i//10)
    else:
        return True


def findAllSuperPrimes(n: int, i: int = 1):
    if i <= n:
        if isPrime(i):
            print(
                {
                    "num": i,
                    "isSuperPrime": isSuperPrime(i, i)
                }
            )
        findAllSuperPrimes(n, i+1)


n = size()

findAllSuperPrimes(n)
