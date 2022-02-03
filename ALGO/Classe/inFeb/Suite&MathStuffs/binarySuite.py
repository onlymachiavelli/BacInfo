

def binary(n: int, i: int = 0, suite: str = "0"):
    if n > 0:
        if i < n:
            if suite[i] == "0":
                toReturn = suite[0:len(suite)] + "01"
            else:
                toReturn = suite[0:len(suite)] + "10"
            return binary(n, i+1, toReturn)
        return suite
    return suite


print(binary(3))


"""
from cgitb import reset
from numpy import binary_repr



"""
