def rec(myString:str):
    for i in range (len(myString) //2) :
        if myString[i] != myString[len(myString) -1 -i] :
            return False 
    return True 

def recString(myString:str,l:int, b:int, e:int) :
    if ( b == e or b+1 == e):
        return True
    else:
        if myString[b] == myString[e] :
            return True and recString(myString,l,b+1,e-1)
        else:
            return False
    
            


a = "liil"
l = len(a)
print(recString(a,l-1,0,l-1))
