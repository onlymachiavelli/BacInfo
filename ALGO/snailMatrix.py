

def fillMat(matrix: any, l, c):
    for i in range(l):
        line = []
        for j in range(c):
            line.append(0)
        matrix.append(line)


def printMat(matrix: any):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="  ")
        print("")


def snailAlgo(matrix: any):
    n = 1
    i = 0
    j = 0
    check = True
    while i < len(matrix) and j < len(matrix):
        matrix[i][j] = n
        n += 1
        j += 1
        if j == len(matrix):
            i += 1
            print(i, j)

            matrix[i][j-1] = n
            n += 1
        if i == len(matrix):
            j -= 1
            matrix[i][j] = n
            check = False
            n += 1
        if not check and j == 0:
            i -= 1
            matrix[i][j] = n
            n += 1
            if matrix[i-1][j] > 0:
                check = True


matrix = []

n = 3
fillMat(matrix, n, n)
snailAlgo(matrix)

printMat(matrix)
