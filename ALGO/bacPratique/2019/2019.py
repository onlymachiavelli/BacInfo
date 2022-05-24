
import numpy as np 

def interval( mi, ma) :
    n = int(input("Enter n ")) 
    if  mi <= n <= ma :
        return n 
    return interval(mi, ma) 



def isPrime(n, i=2):
    if n <2 :
        return False
    if i <= n//2 :
        return n % i != 0 and isPrime(n, i+1) 
    return True




def nums(num, res, n):
    a = num 
    prime  = 2 
    while prime  <= a :
        if a % prime != 0 :
            prime +=1 
            while not isPrime(prime) :
                prime +=1 
        else :
            res[n] = prime
            a //= prime 
            n +=1 

def ppcm(p, q) :
    arr = np.array([int] *a)
    myFile = open("result.dat", "wb") 
    return 0

print(nums(35))