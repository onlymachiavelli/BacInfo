


def size():
    n = int(input("Enter n ")) 
    if  2 <= n <= 100 :
        return n 
    return size()



def ppcm(a,b):
    datas = {
        "a" : "",
        "b" : ""
    }

    n = 2
    na = a
    while na % n != 0:
        print(na)
        if na % n == 0:
            datas["a"] += str(n)
            na //=2
        else :
            n +=1 
            datas["a"] += "/"
    return datas 


print(ppcm(168,24))
