from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dq.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]
        mins = 0
        while dq:
            print(f"Minute {mins}")
            for row in grid:
                for val in row:
                    print(val, end=" ")
                print()
            print(f"dq: {dq}")
            start_len = len(dq)
            new_infected = False
            for _ in range(start_len):
                i, j = dq.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        dq.append((ni, nj))
                        grid[ni][nj] = 2
                        fresh -= 1
                        new_infected = True
            if new_infected:
                mins += 1
        return mins if fresh == 0 else -1
