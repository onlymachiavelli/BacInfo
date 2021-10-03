def word():
    while(1):
        word = input("ENTER THE WORD ")
        if(word.isupper() and word.isalpha() and len(word) in range(3, 11)):
            return word


def find(string: str, target: str):
    for i in range(len(string)):
        if string[i] == target:
            return True
    return None


def fillMat(word: str, mat: list):
    apl = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

    counter = 0
    for i in range(5):
        empty = []
        for j in range(5):
            empty.append(apl[counter])
            counter += 1
        mat.append(empty)


mymat = []

myword = word()


print(mymat)
fillMat(myword, mymat)
print(mymat)
