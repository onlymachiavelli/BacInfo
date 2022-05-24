
import numpy as np 
import pickle as pk 
def interval( mi, ma, msg) :
    n = int(input(msg)) 
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
def count(arr, l , index, check, ele ) :
    nums = 0
    for i in range (l) :
        if check :
            if i != index and arr[i]  == arr[index]:
                nums +=1 
        else :
            if arr[i] == ele :
                nums +=1 
    return nums 
def exist(arr, l , elem ) :
    i =0
    exi = False
    while not exi and i <= l :
        if elem == arr[i] :
            exi = True
    return exi 

def power(a , b) :
    if b > 1 :
        return a * power(a, b-1) 
    return a
def common (arr1, arr2, l1, l2 ) :
    #i know it's stupid  ! 
    res =1 
    big = arr1 
    small = arr2 
    b = l1 
    s = l2 
    if l2 > l1 :
        b = l2 
        s = l1 
        big = arr2 
        small = arr1 
    for i in range (b) :
        if not exist(small , s , big[i]) :
            res *= big[i] 
            print("fucking big of " , big[i])
        else :
            a = count(big, b,i, True , 0)
            bb = count(small, s , 0, False  , big[i]) 

            if a > bb : 
                res *= power(big[i], a)

            else :
                res *= power(big[i], bb) 
    return res
def ppcm( n ) :
    myFile = open("result.dat", "wb") 
    for i in range (n):
        p = interval(1, 1000, "enter p ")
        q = interval(1, 1000 , "enter q ")
        l1 = 0
        l2 = 0
        arr = np.array([int] *(p//2))
        arr2 = np.array([int] * (q//2))

        nums(p, arr, l1) 
        nums(q, arr2, l2) 
        pk.dump({
            "a" : p, 
            "b":q ,
            "ppcm" :common(arr, arr2, l1, l2 ) 
        }, myFile)
    myFile.close()
def Show(n):
    myFile=  open("result.dat" , "rb")  
    for i in range (n):
        obj = pk.load(myFile)
        print("PPCM(", obj["a"] , ",",obj["b"] , ") = " , obj["ppcm"])
    myFile.close()


n = interval(2 , 100, "enter n ")

ppcm(n )
Show(n)