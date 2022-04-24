from math import *


def apprx(ep):
    i = 1
    s = 0
    s1 = 0
    quit = False
    while (not quit):
        s = s1
        s1 += 1/i**2
        i += 1
        quit = sqrt(s1*6) - sqrt(s*6) > ep
    return sqrt(s1*6)


print(apprx(0.0001))
