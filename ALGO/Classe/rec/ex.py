m = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


for i in range(len(m)):
    for j in range(i+1):
        if j == 0 or i == j:
            m[i][j] = 1
        else:
            m[i][j] = m[i-1][j] + m[i-1][j-1]


for i in range(len(m)):
    print(m[i])


print(2**5)
