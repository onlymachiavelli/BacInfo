from dis import dis
from re import L
import numpy as np 
import pickle as pk 
def distinct(myString): 
    toReturn = True 
    for i in range (len(myString)) :
        for j in range (len(myString)) :
            if i != j and myString[i] == myString[j] :
                toReturn = False 
    return toReturn

def salt() :
    key = input("Enter the salt ! ")
    check = True  
    for i in range (len(key)) :
        if key[i] > "Z" or key[i] < "A" :
            check = False 
    if check and distinct(key) and 5 <= len(key) <= 10 :
        return key
    return salt()

def getLines(source):
    myFile =open(source, "r" )
    size = 0
    while myFile.readline() :
        size +=1 
    myFile.close()
    return size 

def fillSaces(arr, l, c ) :
    for i in range (l) :
        for  j in range (c) :
            arr[i,j] = " " 
def crypt(source, key) : 
    myFile = open(source, "r") 
    result = open("crypt.txt" , "w") 

    lines = getLines(source )
    for i in range (lines) : 
        line = myFile.readline()
        line = line[0:len(line)-1]
        while len(line) % len(key) != 0 :
            line += " " 
        res = "" 
        l = len(line) 
        c = len(key)
        arr = np.array([[str()] * c ] *l) 
        fillSaces(arr, l, c )
        print(arr)
        matLine = 1 
        for k in range(len(key)) :
            arr[0,k] = key[k]
        pos = 0 
        
        while pos < len(line) :
            select = line[pos:pos+len(key)] 
            for k in range (len(select)) :
                arr[matLine,k] = select[k]
                print(f"fuck {matLine} and the shit is {arr}")
            matLine +=1 



            pos += len(key)
        for k in range (c) :
            bug = "" 
            for j in range (l//len(key)) :
                bug += arr[j,k]
            res += bug
            
        result.write(res+ "\n")
    myFile.close()
    result.close()
key = salt() 
source = "source.txt" 
crypt(source, key) 
