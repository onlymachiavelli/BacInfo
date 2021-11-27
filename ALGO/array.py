"""
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


def bubble_recursive(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            bubble_recursive(array)


def SelectionSort(t, n: int):
    for i in range(1, n):
        tmp = t[i]
        j = i
        while j >= 1 and tmp < t[j-1]:
            t[j] = t[j-1]
            j = j-1
        t[j] = tmp


def ShellSort():

    return 0


myarr = [4, 1, 7, 5, 0, 8]

SelectionSort(myarr, len(myarr))

print("This is a selection SORT !")
print(myarr)

#arr1 = np.arange(15, dtype=int)


# for i in range(15):
#    arr1[i] = r.randint(1, 100)

# BubbleSort(arr1)


# Show(arr1)

"""
