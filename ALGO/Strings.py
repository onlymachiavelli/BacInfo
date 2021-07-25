#These are some stupid basic algorythms, 
#Im keeping the syntax simple so ur ass can understand lmao  
#To reverse a freaking string : 
def RevString(string:str):
    i = len(string)
    newString = ""
    while (i != 0):
        i -= 1
        newString += string[i]
    return newString

print(RevString("hello world"))



#search in string
def FindS(string:str, ele:str):
    for i in range (len(string)):
        if(string[i] == ele): return i
    return -1 #means Doesnt exist 

print(FindS("hello", "y"))

#Does the string start with ...
def StartWith(string:str, start:str):
    for i in range (len(start)):
        if (string[i] != start[i]):return False
    return True
print(StartWith("fuck", "fu"))