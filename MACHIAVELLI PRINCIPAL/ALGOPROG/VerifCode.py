def enter():
    code = input("Enter code ! ") 
    check = True 
    for i in range (len(code)) :
        if not code[i].isdecimal() :
            check = False
    if check and len(code) == 13 :
        return code 
    return enter() 
def FromDec(code) :
    res = ""    
    cd = code 
    while cd > 0 :
        res = str(cd % 2) + res 
        cd = cd //2
    return res 

def getLine(source):
    myFile = open(source, "r")
    n = 0
    while myFile.readline():
        n +=1 
    return n 

def exist(source, code):
    n = getLine(source) 
    check = False 
    myfile= open(source, "r")
    for i in range (n) :
        if i < n :
            line = myfile.readline()
            if code == line[0:len(code) ] :
                check = True 
    myfile.close() 
    return check
def isPrime(p, i):
    if p <= 1 :
        return False 
    if i < p//2 :
        return p % i != 0 and isPrime(p, i+1) 
    return True 
def coun(code) :
    n=0
    for i in range (len(code)) :
        if code[i] == "0" :
            n+=1 
    return n 
def verifcode(code) :
    verified = True 

    left = code[0:3]
    mid= code[3:8]
    right= code[8:len(code)] 

    if not isPrime(int(left),2) :
        verified = False
    binCode = FromDec(int(mid))
    if coun(binCode) < 8 :
        verified = False 
    if int(right) % int(left) != 0 :
        verified = False 
    return verified 

def result(source, code) :
    if verifcode(code) and exist(source, code) :
        print("Code validee") 
    elif verifcode(code) and not exist(source, code):
        print("code deja utilisee")
    else :
        print("code non validee ") 
code = enter()
source = "Code.txt"
result(source, code) 