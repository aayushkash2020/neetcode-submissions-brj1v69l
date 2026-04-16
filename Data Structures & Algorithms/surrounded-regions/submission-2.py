class Solution:      
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'B'
            for di, dj in dirs:
                dfs(i + di, j + dj)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'
        
        # m, n = len(board), len(board[0])
        # def print_grid():
        #     for i in range(m):
        #         for j in range(n):
        #             print(board[i][j], end=' ')
        #         print()
        # print("original:")
        # print_grid()
        # print()
        # dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # def isSurrounded(i, j):
        #     stack = [(i, j)]
        #     region = []
        #     surrounded = True

        #     while stack:
        #         x, y = stack.pop()

        #         if x < 0 or x >= m or y < 0 or y >= n:
        #             surrounded = False
        #             continue

        #         if board[x][y] != 'O':
        #             continue

        #         board[x][y] = 'V'
        #         region.append((x, y))

        #         for dx, dy in dirs:
        #             stack.append((x+dx, y+dy))

        #     # finalize
        #     for x, y in region:
        #         board[x][y] = 'X' if surrounded else 'O'

        #     return surrounded
            
        # for i in range(m):
        #     for j in range(n):
        #         isSurrounded(i, j)
        # print("final:")
        # print_grid()
