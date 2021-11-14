
from pickle import *
import pickle


def Exist(ele: str):
    myFile = open("compte.txt", "r")
    Lines = myFile.readlines()
    return ele in Lines


def fillMVT():
    global n
    fc = open("compte.txt", "r")
    fv = open("mvt.dat", "wb")
    quit = False

    while not quit:
        n += 1
        q = False
        while not q:
            num = input("enter Number ")

            q = Exist(num)

        q = False
        while not q:
            day = input("Enter the day ")
            month = input("Enter month ")
            year = input("Enter year ")

            q = len(day) == 2 and day.isnumeric() and len(
                month) == 2 and month.isnumeric() and len(year) == 4 and year.isnumeric()
        date = day+"/"+month+"/"+year

        q = False
        while not q:
            mont = float(input("Enter mont "))
            q = mont > 0
        q = False
        while not q:
            nat = input("Enter nat ")
            q = nat == "D" or nat == "C"

        pickle.dump(fv, {
            "num": num,
            "date": date,
            "mont": mont,
            "nat": nat
        })

        print("Do you ant to add anther one ?  y/anything else")
        ans = input()
        quit = ans.upper() == "Y" or "YES"


def fillRes(n: int):
    fs = open("result.txt", "w")
    fv = open("mvt.dat", "rb")

    datas = []
    quit = False
    while not quit:
        try:
            o = pickle.load(fv)

        except:
            quit = True
