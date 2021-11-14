

from os import readlink


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
                month) == 2 and month.isnumeric() and len(year) == 4
