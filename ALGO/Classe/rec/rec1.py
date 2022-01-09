def isPrime (n:int, i:int = 1):
    if n // 2 == i :
        return True
    else :
        return True and n%i != 0 and isPrime(n, i+1) 


print(isPrime(4))