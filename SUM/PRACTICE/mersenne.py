from pickle import TRUE


def size(min, max ) :
    n = int(input("Enter N"))
    if min < n < max :
        return n 
    return size(min, max)



def isPrime(n):
    toReturn = True
    if n >1 :
        for i in range (n//2) :
            if n% i==0:
                toReturn = False 


    return False 

def mersenne(a,b):
    for i in range (a,b):
        pass
a  = size(2,5000)
b = size(a,5000)

