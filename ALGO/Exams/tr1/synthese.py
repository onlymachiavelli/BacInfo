import random as r 
from pickle import *
import numpy as np 


def fillMat (m:np.ndarray,l:int, c:int ):
    for i in range (l):
        for j in range (c):
            num = r.randint(-99, 100)
            

values = input("Enter the lengths ").split()
l, c = map(int , values)

mat = np.zeros([l,c], dtype=int)
print(mat)

print(type(mat))