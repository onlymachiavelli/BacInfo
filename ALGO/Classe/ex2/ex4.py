def word():
    while(1):
        word = input("ENTER THE WORD ")
        if(word.isupper() and word.isalpha()):
            return word


def fillMat(word, mat: list):
    actuallist = []
    apl = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
