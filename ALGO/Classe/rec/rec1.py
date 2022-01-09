def rev (stri, n):
    if n >= 0 :
        return stri[n] + rev(stri, n-1)
a = ["h","e","l","l","o"]
l = len(a) -1
print(rev(a,l))