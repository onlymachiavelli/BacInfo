from Strings import RevString # i just imported this file so i can reverse some strigns


#to conv from decimal to binary :
def Bin(num:int):
    string = ""
    while num!= 0:
        if num%2 == 0: string += "0"
        else : string += "1"
        num //= 2
    return RevString(string)


print(Bin(600))