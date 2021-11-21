import pickle


fs = open("dick.dat", "rb")

mohsen = []
quit = False
while not quit :
    try:
        mohsen.append(pickle.load(fs))
    except:
        quit = True
print(mohsen)
fs.close()












"""
text files

data files


"""













"""

import numpy as np
import random as r
def sasir():
    quit = False
    while not quit:
        n = int(input("Enter n "))
        quit = 3 <= n <= 15
    return n


def remplirf1(n):
    fs = open("source.txt", "w")
    for i in range(n):
        quit = False
        while not quit:
            ch = input("Enter numbers of line " + str(i+1) + " ")
            quit = ch.isnumeric() and len(ch) > 0
        fs.write(ch+"\n")
    fs.close()

def remplirM(n, m):
    fs = open("source.txt", "r")
    lines = fs.readlines()
    for i in range (n):
        lines[i] = lines[i][:len(lines[i])-1]
        while len(lines[i]) < n :
            lines[i] = str(r.randint(0,10)) + lines[i]
        for j in range(n):
            m[i][j] = lines[i][j]
        
        
def triselect(n,mat,p):
    for i in range(n-1):
        m = i
        for j in range (i+1, n):
            if mat[p][j] < mat[p][m] :
                m = j
                tmp = mat[p][m]
                mat[p][m] = mat[p][i]
                mat[p][i] = tmp
                m = i

def TriSelection(n,m):
    for i in range (n):
        triselect(n,m,i)
        
def remplirfe(n, m):
    fe= open("source.txt", "w")
    
    for j in range (n):
        ch = ""
        for i in range (n):
            ch  += m[i][j]
            
        fe.write(ch + "\n")
    fe.close()
# PP
n = sasir()
m = np.array([[""]*n] *n, dtype=str)

remplirf1(n)
remplirM(n,m)
TriSelection(n,m)
remplirfe(n, m)
print(m)




"""