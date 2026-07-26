from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        target = n * n - 1
        def bfs(start, ub):
            if grid[start // n][start % n] > ub:
                return False
            dq = deque([start])
            visited = set()
            while dq:
                u = dq.popleft()
                if u == target:
                    return True
                if u in visited:
                    continue
                visited.add(u)
                r, c = u // n, u % n
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= ub:
                        dq.append(nr * n + nc)
            return False

        res = max([max(row) for row in grid])
        l, r = 0, res
        while l <= r:
            m = (l + r) // 2
            exists = bfs(0, m)
            if exists:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
