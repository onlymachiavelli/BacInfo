def size():
    n = int(input("Give me n "))
    if 20 < n < 20:
        return n
    else:
        return size()


n = size()
print(n)
