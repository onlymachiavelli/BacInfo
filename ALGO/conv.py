from Strings import RevString # i just imported this file so i can reverse some strings


#to conv from decimal to binary :
def Bin(num:int):
    string = ""
    while num!= 0:
        if num%2 == 0: string += "0"
        else : string += "1"
        num //= 2
    return RevString(string)

#to convert from binary to  decimal
def Dec(string:str):
    summ = 0
    i = len(string)
    j = 0
    while (i != 0):
        i -=1
        summ += int(string[j])* (2**i)
        j +=1
    return summ




#to convert octal to binary
def OctBin(num:int):
    res = ""
    s = str(num)
    b = ""
    for i in range(len(s)):
        b = Bin(int(s[i]))
        if len(b) < 3 :
            for j in range (3-len(b)): b = "0"+b
        res += b
    return res[1: len(res)]
        
print(Dec("1001011000"))
print(Bin(600))
print(OctBin(35))
