import numpy as np 

import pickle as pk 

def getN(code):
    if code.isdecimal() :
        return int(code)

    return ord(code) - 55

def power(a,b) :
    if b > 1 :
        return a * power(a, b-1)
    return a

def toDec(code, base) :
    res = 0 
    for i in range(len(code)) :
        res += power(base, i) * getN(code[len(code) -1-i])
        print(getN(code[len(code) -1-i]))

    return res


print(toDec("A", 16))


