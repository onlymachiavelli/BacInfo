import numpy as np
import random as r


def receiveTxt():
    while True:
        text = input("Enter the text ")
        if 0 < len(text) <= 18:
            return text


def fillMat(mat):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(6):
        for j in range(6):
            mat[i][j] = r.choice(alpha)[0]


def cryptMsg(text: str, mat):
    secret = ""
    x = "ABCDEF"
    ind = 0
    while (ind != len(text)):
        ind += 1
        for i in range(6):
            for j in range(6):
                if text[ind] == mat[i][j]:
                    secret += x[i] + x[j]
                if text[i] == " ":
                    secret += " "
    return secret


def fillS_cnd_Mat(secret: str, mat, key: str):
    return 0


mat = np.array([[""]*6]*6, dtype="str")
matCrypt = np.array([[""]*6]*6, dtype="str")


fillMat(mat)
text = receiveTxt()
print(cryptMsg(text, mat))
