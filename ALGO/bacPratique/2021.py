import numpy as np 
def getN(code):
    if(not code.isdecimal()):
        return ord(code) - 55
    return int(code)


def power(a,b):
    res = 1
    for i in range(b):
        res *= a
    return res 
def toDec(code):
    dec = 0
    for i in range(len(code)) :
        dec += power(16, len(code)-i-1) * getN(code[i])
    return dec 

def getLines():
    myFile = open("imgHexa.txt" ,"r")
    lines = 0
    while myFile.readline() :
        lines += 1 
    myFile.close()
    return lines 


def sort(t,n):
    quit = False
    while not quit : 
        quit = True 
        for i in range (n-1):
            if t[i]["Dec"] > t[i+1]["Dec"] :
                flip = t[i] 
                t[i] = t[i+1] 
                t[i+1] = flip
                quit = False 
 

def gen(nb):
    n = nb
    word = ""
    quit = False 
    while not quit  :
        
        r = n % 3
        print(r)
        if(r ==0) :
            word += "Ma"
        elif r == 1 :
            word += "Des" 
        elif r ==2 :
            word += "Son"
        n = n//2
        quit = r == 0
        
    return word 



def crypt(t, n):
    myFile = open("imgHexa.txt", "r")
    Line = 1
    for i in range (n):
        hexa = myFile.readline()
        t[i] = {
            "Hex" : hexa,
            "Num" : Line,
            "Dec" : toDec(hexa) 
        }
        Line +=1 
    myFile.close()

    myFile = open("result.txt" , "w")

    sort(t,n)
    for i in range (n):
        myFile.write(gen(t[i]["Dec"]) + " " + str(t[i]["Num"]) + "\n")
    myFile.close()


arr = np.array([{}]*getLines())



n = getLines()
crypt(arr,n)