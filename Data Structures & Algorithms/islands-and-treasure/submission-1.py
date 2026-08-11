from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        inf = 2 ** 31 - 1
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dq.append((i, j, 0))
        while dq:
            i, j, d = dq.popleft()
            for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == inf:
                    dq.append((ni, nj, d+1))
                    grid[ni][nj] = d+1
