

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


def snailAlgo():

    return 0


matrix = []

n = 5
fillMat(matrix, n, n)


printMat(matrix)
