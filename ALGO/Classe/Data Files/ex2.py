<<<<<<< HEAD
def fillFc(n):
    myFile = open("commande.txt", )
 ( ) [ ]
=======
from pickle import *

def remplirfc():
    global n
    myFile = open("commande.dat", "wb")
    n = 0
    quit = False
    while not quit:
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
      myFile)
      n += 1
      print("Would you like to keep going ? Y if you want to keep or something else if you want to stop ")
      ans = input().upper()
      quit = ans ==  "Y"
    myFile.close()
def Gen(n:int):
    data = open("commande.dat", "rb")
    bill = open("bill.txt", "w")
    
n = 0
        
    
            
>>>>>>> 7c158388bc898ea8d0f9cb98df14fa782ce72482
