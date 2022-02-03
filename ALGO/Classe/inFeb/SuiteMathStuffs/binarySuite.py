

def binary(n: int, i: int = 0, suite: str = "0"):
    if n > 0:
        if i < len(suite):
            toReturn = ""
            if suite[i] == "0":
                toReturn = suite[0:i-1] + "01" + suite[i: len(suite)]
            else:
                toReturn = suite[0:i-1] + "10" + suite[i: len(suite)]
            return binary(n, i+1, toReturn)
        else:
            return binary(n-1, 0, suite)
    return suite


print(binary(3))


"""
from cgitb import reset
from numpy import binary_repr



"""
