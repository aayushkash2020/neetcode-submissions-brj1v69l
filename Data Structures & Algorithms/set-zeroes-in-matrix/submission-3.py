class Solution:
    def printMat(self, matrix):
        for row in matrix:
            for val in row:
                print(val, end=" ")
            print()
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_0 = any(matrix[0][j] == 0 for j in range(n))
        first_col_0 = any(matrix[i][0] == 0 for i in range(m))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        if first_row_0:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_0:
            for i in range(m):
                matrix[i][0] = 0
        