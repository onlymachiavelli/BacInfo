#These are some stupid basic algorythms, 
#To reverse a freaking string : 
def RevString(string:str):
    i = len(string)
    newString = ""
    while (i != 0):
        i -= 1
        newString += string[i]
    return newString

print(RevString("hello world"))