import pickle as pck 
import numpy as np 
import random as r 

def size (min, max) :
    n = int(input("Enter the number "))
    if min <= n <= max :
        return n
    return size(min, max)


def pairSize():
    n = size()
    if n % 2 ==0 :
        return n
    return pairSize()


def fillMat(mat, n,m):
    mat = np.array([[(int)]*m]*n)
    for i in range (n):
        for j in range (m):
            mat[i,j] = r.randint(-20, 70)
    return mat 

def genFile(src, n, m,mat):
    myFile = open(src , "wb")
    for i in range (n) :
        for j in range (m//2) :
            pck.dump(
                abs(mat[i,j]-mat[i,m-1-j]),
                myFile
            )



n = size()
m = pairSize()
mat = fillMat()



