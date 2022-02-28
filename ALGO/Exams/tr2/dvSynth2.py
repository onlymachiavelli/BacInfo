import numpy as np


def size(minimum: int, maximum: int):
    n = int(input("Enter The Size ! "))
    if minimum < n < maximum:
        return n
    return size(minimum, maximum)
