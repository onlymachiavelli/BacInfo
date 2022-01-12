def size():

    n = int(input("Enter n "))
    quit = 40000 < n < 100000
    if quit:
        return n
    else:
        return size()


def isPrime(n: int, i: int = 2):
    return 0
