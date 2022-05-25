import numpy as np 
import pickle as pk 
def size(mi, ma) :
    n = int(input()) 
    if mi <= n <= ma :
        return n 
    print("Enter it again ! ")
    return size(mi, ma )


def isPrime(n, i=2):
    if n <2 :
        return False
    if i <= n//2 :
        return n % i != 0 and isPrime(n, i+1) 
    return True

def fillPrimeNumbers (primi, l, n) :
    prime = 2
    l = n//2
    for i in range (l) :
        primi[i] = prime 
        prime +=1 
        while not isPrime(prime) :
            prime +=1 

def getPrime(primi,arr1,l1,  n) :
    prime =primi[0]
    number = n
    count = 0
    l = 0
    while number >= prime :
        if number % prime != 0 :
            l+=1 
            prime = primi[l]
            arr1[l1] = count 
            l1+= 1 
            count = 0
        
        else :
            count +=1 
            number //= prime
def power(a , b) :
    if b > 1 :
        return a * power(a, b-1) 
    return a

def ppcm(p, q) :
    thePrimes = np.array([int] * 100)# array of prime numbers 
    primeLen = 0
    fillPrimeNumbers(thePrimes,primeLen, (p+q)//2 )
    arr1 = np.array([int] * 100 ) # array of the numbers of p 
    arr2 = np.array([int] * 100 )# array of the numbers of q
    len1= 0
    len2 = 0
    getPrime(thePrimes, arr1 , len1, p)
    getPrime(thePrimes, arr2 , len2, q)
    res =1 
    big = arr1 
    small = arr2 
    b = len1 
    s = len2
    if len1 < len2 :

        big = arr2 
        small = arr1
        b = len2
        s = len1
    print (s< b)
    while b != s :
        s+=1 
        small[s] = 0

    for i in range (b):
        if big[i] > 0 and small[i] > 0 :
            if big[i] > small[i] :
                res *= power(thePrimes[i], big[i])
        else :
            res *= power(thePrimes[i], small[i])
    return res 

def saveFile(n) :
    myfile = open("result.dat", "wb")
    for i in range (n) :
        print("Give  p ") 
        p = size(1, 1000)
        print("Give q ")
        q = size(1 , 1000)
        pk.dump({
            "a" : p, 
            "b" : q ,
            "ppcm" : ppcm(p,q) 
        }, myfile)

    myfile.close()

def Show(n):
    myFile=  open("result.dat" , "rb")  
    for i in range (n):
        obj = pk.load(myFile)
        print("PPCM(", obj["a"] , ",",obj["b"] , ") = " , obj["ppcm"])
    myFile.close()


print("Enter n ! ")
n = size(2 , 100)
saveFile(n)
Show(n)