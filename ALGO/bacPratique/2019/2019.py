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

def fillPrimeNumbers (primi, n) :
    prime = 2
    for i in range (n) :
        primi[i] = prime 
        prime +=1 
        while not isPrime(prime) :
            prime +=1 

def getPrime(primi,arr1,n) :
    prime =primi[0]
    number = n
    count = 0
    l = 0
    le = 0
    while n >= prime :
        if number % prime != 0 :
            l+=1 
            prime = primi[l]
            arr1[le] = count 
            le+= 1 
            count = 0
        
        else :
            count +=1 
            number //= prime

def power(a , b) :
    if b > 1 :
        return a * power(a, b-1) 
    return a

def init(arr, length):
    for i in range (length):
        arr[i] = 0 


def ppcm(p, q) :
    n = (p+q) //2
    print(n)
    thePrimes = np.array([int] * n)# array of prime numbers 
    fillPrimeNumbers(thePrimes, n )
    arr1 = np.array([int] * n ) # array of the numbers of p 
    arr2 = np.array([int] * n )# array of the numbers of q
    init(arr1, n )
    init(arr2, n )
    getPrime(thePrimes, arr1 , p)
    getPrime(thePrimes, arr2 , q)
    print(arr1)
    res =1 


    for i in range (n):
        if arr1[i] > 0 or arr2[i] > 0 :
            if arr1[i] > arr2[i] :
                res *= power(thePrimes[i],arr1[i])
            else :
                res *= power(thePrimes[i],arr2[i])
        
                
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


