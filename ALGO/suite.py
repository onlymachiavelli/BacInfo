# binary solution
def suite(n: int, st: str, i: int = 0):
    if n > 0:
        if i < len(st):
            if st[i] == "0":
                return suite(n, st[0:i] + "01"+st[i+1:len(st)], i+2)
            else:
                return suite(n, st[0:i] + "10"+st[i + 1:len(st)], i+2)
        else:
            return suite(n-1, st, 0)
    return st


print(suite(3, "0", 0))
