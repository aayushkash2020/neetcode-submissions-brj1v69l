"""
123
456
789

147
258
369

741
852
963


"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        for i in range(n):
            a, b = 0, n-1
            while a <= b:
                matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
                a += 1
                b -= 1