import numpy as np
import random as r


def size(mi, ma):
    n = int(input("Enteer N \n "))
    if mi <= n <= ma:
        return n
    return size(mi, ma)
