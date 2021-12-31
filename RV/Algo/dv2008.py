print("hello world")


def f(x: float, n: int, t: list):
    i = 0
    while x != t[i] and i < n:
        i += 1
        print(i)
    return x == t[i]


t = [2.5, 3, 100, 99, 5, 3.7, 0, 5]

print(f(2, len(t), t))
