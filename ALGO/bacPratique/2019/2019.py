
import numpy as np 
import pickle as pk 


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
            res *= small[i] 
        else :
            a = count(big, b,i)
            b = 0
            


    return 0

print(power(2,5))

def ppcm(p, q, n ) :
    myFile = open("result.dat", "wb") 
    for i in range (n):
        res = 1 
        l1 = 0
        arr = np.array([int] *p)
        l2 = 0
        arr2 = np.array([int] * q)
        nums(p, arr, l1) 
        nums(q, arr2, l2) 


        pk.dumpy({
            "a" : p, 
            "b":q ,
            "ppcm" :res 
        }, myFile)





        
    


    myFile.close()
    


def Show():
    myFile=  open("result.dat" , "wb")  
    quit = False 
    while not quit : 
        try :
            obj = pk.load(myFile) 
            print("PPCM(", obj["a"] , ",",obj["b"] , ") = " , obj["res"])

        except:
            quit = True 

    myFile.close()
print(nums(35))