def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:

    if H1 < H2 or W1 < W2:
        return False

    matrix1 = matrix(S1)
    matrix2 = matrix(S2)
    
    flag = False
    for i in range(H1):
        for j in range(W1):
            if matrix2[0][0] == matrix1[i][j] and i + H2 - 1 <= H1 and j + W2 - 1 <= W1:
                row, column = i, j
                flag = comparison(matrix1,  H2, W2, matrix2, row, column)
            if flag:
                return flag
    return flag

def matrix(s: str):
    l1 = s.split()
    matrix = []
    for s in l1:
        l2 = []
        for i in s:
            l2.append(i)
        matrix.append(l2)
    return matrix

def comparison(matrix1: list, H2: int, W2: int, matrix2: list, row: int, column: int):
    
    for i in range(H2):
        for j in range(W2):
            if matrix2[i][j] != matrix1[row + i][column + j]:
                return False
    return True