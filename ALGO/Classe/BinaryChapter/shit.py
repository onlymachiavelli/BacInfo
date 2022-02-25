def size(minimum: int, maximum: int):
    n = int(input("Enter N"))
    if minimum < n < maximum:
        return n
    return size(minimum, maximum)


def isPrime(n: int, i: int = 2):
    if n > 1:
        if i <= n//2:
            return n % i != 0 and isPrime(n, i+1)
        return True
    return False


def result(a: int, b: int):
    myFile = open("result.txt", "w")
    for i in range(a, b+1):
        pre = 2
        res = 0
        check = False
        while res < i:
            if not isPrime(pre):
                pre += 1
            else:
                res = (2 ** pre) - 1
        if check:
            myFile.write(str(i) + " Est mersenne ")
        else:
            myFile.write(str(i) + " Est non  mersenne ")
    myFile.close()
