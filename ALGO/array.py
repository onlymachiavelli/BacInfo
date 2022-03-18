def Bubble(arr, n):
    check = False
    while not check:
        check = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                check = False


def bubRec(arr, n):
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            bubRec(arr, n)


def Selection(arr, n):
    for i in range(1, n):
        tmp = arr[i]
        j = i
        while j >= 1 and tmp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1

        arr[j] = tmp


b = [3, 7, 9, 1]


def ShellSort(arr, n):
    interv = n // 2
    while interv > 0:
        for i in range(interv, n):
            swap = arr[i]
            j = i
            while j >= interv and arr[j - interv] > swap:
                arr[j] = arr[j - interv]
                j -= interv

            arr[j] = swap
        interv //= 2


# bubRec(b, len(b))
print("This is a shell sort ")
ShellSort(b, len(b))
print(b)
# a = [69, 2, 7, 20, 3]
# Bubble(a, len(a))
# print(a)
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

# arr1 = np.arange(15, dtype=int)


# for i in range(15):
#    arr1[i] = r.randint(1, 100)

# BubbleSort(arr1)


# Show(arr1)

"""
