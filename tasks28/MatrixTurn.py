from typing import List

def MatrixTurn(Matrix: List[str], M: int, N: int, T: int) -> None:

    matrix = []
    for i in range(M):
        matrix_col = []
        for j in range(N):
            matrix_col.append(Matrix[i][j])
        matrix.append(matrix_col)

    for i in range(T):
        rotate(matrix, M, N)
    
    Matrix = []
    for i in range(M):
        s = ''
        for j in range(N):
            s += ''.join(matrix[i][j])
        Matrix.append(s)
    
def rotate(matrix, M, N):

    row_start = 0
    row_end = M - 1
    column_start = 0
    column_end = N - 1

    while row_start < row_end and column_start < column_end:

        num1 = matrix[row_start + 1][column_start]
        for i in range(column_start, column_end + 1):
            num2 = matrix[row_start][i]
            matrix[row_start][i] = num1 
            num1 = num2
        row_start += 1

        for i in range(row_start, row_end + 1):
            num2 = matrix[i][column_end]
            matrix[i][column_end] = num1
            num1 = num2
        column_end -= 1

        for i in range(column_end, column_start - 1, -1):
            num2 = matrix[row_end][i]
            matrix[row_end][i] = num1
            num1 = num2
        row_end -= 1

        for i in range(row_end, row_start - 1, -1):
            num2 = matrix[i][column_start]
            matrix[i][column_start] = num1
            num1 = num2
        column_start += 1

    return matrix