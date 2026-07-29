class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # def dfs(r, c):
        #     res = 0
        #     st = [(r, c)]
        #     while st:
        #         i, j = st.pop()
        #         if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
        #             continue
        #         grid[i][j] = 0
        #         res += 1
        #         for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        #             st.append((i + di, j + dj))
        #     return res
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            res = 1
            for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                res += dfs(i + di, j + dj)
            return res
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
            