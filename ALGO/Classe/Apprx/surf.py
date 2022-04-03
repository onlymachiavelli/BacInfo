import math


def f(x: float):
    return math.cos(x) + math.sqrt(x)


def surf(n: int, a: float, b: float):
    s = 0
    h = (b-a)/n
    x = a + h/2
    for i in range(n):
        s += f(x) * h
        x += h
    return s


a = 1
b = 4
#print(surf(10000, a, b))
arr = [
    {"type": "gauche", "val": 3.0684222885524766},
    {"type": "droite", "val": 3.0683641047744574},
    {"type": "milieu", "val": 3.068393181495397},
    {"type": "trap", "val": 3.0683641199449028},
]


def trap(n: int, a: float, b: float):
    s = 0
    h = (b-a)/n
    x = a + h/2
    for i in range(n):
        s += (f(x) + f(x+h))*(h/2)
        x += h
    return s


print(trap(10000, a, b))

minn = arr[0]
for i in range(len(arr)):
    if minn["val"] < arr[i]["val"]:
        minn = arr[i]
print(minn)

"""

n = 10000
gauche -> 3.0684222885524766
droite -> 3.0683641047744574
milieu -> 3.068393181495397
droite 


f(x) = cos(x) + racine(x)
a = 1 
b = 4 
minn = arr[0]
for i in range(len(arr)):
    if minn["val"] < arr[i]["val"]:
        minn = arr[i]
print(minn)
"""
