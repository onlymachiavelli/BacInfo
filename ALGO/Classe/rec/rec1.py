def rec(myString:str):
    for i in range (len(myString) //2) :
        if myString[i] != myString[len(myString) -1 -i] :
            return False 
    return True 



