

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
    limitHor = len(matrix)
    limVert = len(matrix[0])
    num = 0
    i = 0
    j = 0
    while limitHor > 0 and limVert > 0:
        matrix[i][j] = num


matrix = []

n = 5
fillMat(matrix, n, n)


printMat(matrix)
