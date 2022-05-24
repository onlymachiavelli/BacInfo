def size(mi, ma) :
    n = int(input()) 
    if mi <= n <= ma :
        return n 
    return size(mi, ma )


def isPrime(n, i=2):
    if n <2 :
        return False
    if i <= n//2 :
        return n % i != 0 and isPrime(n, i+1) 
    return True

def ppcm(a, b ) :
    res = 1 
    p =a 
    q = b 
    pa = 2 
    pb = 2 
    ca = 0
    cb = 0


    while p > pa and b > pb : 
        



        return res 