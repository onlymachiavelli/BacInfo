
import pickle
from math import sqrt


def size():

    n = int(input("Enter n "))
    if 40000 < n < 100000:
        return n
    return size()


def isPrime(n: int, i: int = 2):
    if i > sqrt(n):
        return True
    return n % i != 0 and isPrime(n, i + 1)


def mainFunc(n: int):
    myFile = open("theResult.dat", "wb")
    for i in range(1, n):
        a = i
        counter = [0, 1]
        while a > 1:
            if isPrime(i):
                counter[0] += 1
                if isPrime(a):
                    counter[1] += 1
                res = {
                    "Num": a,
                    "isSuperPrime": counter[0] == counter[1],

                }
                myFile.dump(
                    res, myFile
                )
                print(res)
                a //= 10
    myFile.close()


n = size()
mainFunc(n)
