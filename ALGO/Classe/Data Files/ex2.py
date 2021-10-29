from pickle import *

def remplirfc(n):
    
    myfile = open("commande.dat", "wb")
    n = 0
    quit = False
        while(not quit):
            name = input("enter name ")
            qte = int(input("Enter qte "))
            price = float(input("Enter price "))
            state = bool(input("Enter 1 : True or 0 : False"))
            dump(
                {
                    "name":name,
                    "qte":qte,
                    "price":price,
                    "state":state,
                    },
                myFile
                )
            n += 1
            print("Would you like to keep going ? Y if you want to keep or something else if you want to stop ")
            ans = input().upper()
            quit = answer ==  "Y"
        myFile.close()
def Gen(n:int):
    data = open("commande.dat", "rb")
    bill = open("bill.txt", "w")
    
        
    
            