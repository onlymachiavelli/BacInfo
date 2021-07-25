import numpy as np
import random as r

arr1 = np.arange(15, dtype=int)

#booring way to print the array 
def Show(array):
    for i in range (len(array)): print(array[i], end=",")


#Bubble Sort
def BubbleSort(array):
    check = False
    while(not check):
        check = True 
        for i in range (len(array)-1):
            if array[i] > array[i+1] :
                array[i], array[i+1] = array[i+1] , array[i]
                check = False

for i in range (15):
    arr1[i] = r.randint(1, 100)

BubbleSort(arr1)
Show(arr1)

