def defN():
    n = int(input("Enter N "))
    if 400 < n < 1000:
        return n
    return defN()


def defM(n: int):
    m = int(input("Enter M "))
    if 400 < m < n < 1000:
        return m
    return defM(n)


def isPrime(n: int, i: int = 2):
    if n > 1:
        if i <= n//2:
            if n % i == 0:
                return False
            return isPrime(n, i+1)
        return True

    else:
        return False


def Primo(n: int):
    i = 1
    res = 1
    ch = ""
    op = ""
    while res < n:

        i += 1
        if isPrime(i):
            res *= i
            ch += str(i) + "*"
        if res - 1 == n:
            res -= 1
            op = "-"
        if res + 1 == n:
            res += 1
            op = "+"
    ch = ch[0:len(ch) - 1]
    ch = str(i) + "#" + op + "1 = " + ch
    return ch


def saveFile(n: int, m: int, src: str):
    myFile = open(src, "w")

    i = m
    while i <= n:
        if not isPrime(i):
            print(i)
            myFile.write(Primo(i) + "\n")
        i += 1

    myFile.close()


n = defN()
m = defM(n)
saveFile(n, m, "result.txt")
