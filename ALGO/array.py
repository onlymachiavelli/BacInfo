import numpy as np
import random as r


# booring way to print the array


def Show(array):
    for i in range(len(array)):
        print(array[i], end=",")


# Bubble Sort
def BubbleSort(array):
    check = False
    while(not check):
        check = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                check = False


def SelectionSort(t: list, n: int):
    for i in range(n-1):
        getMax = i
        for j in range(i, n-1):
            if(t[i] > t[i+1]):
                getMax = j
        t[i], t[getMax] = t[getMax], t[i]


def ShellSort():

    return 0


myarr = [4, 1, 7, 5, 0, 8]

SelectionSort(myarr, len(myarr))

print("This is a selection SORT !")
print(myarr)

arr1 = np.arange(15, dtype=int)


for i in range(15):
    arr1[i] = r.randint(1, 100)

BubbleSort(arr1)
Show(arr1)
