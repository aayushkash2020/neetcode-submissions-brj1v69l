from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # for row in grid:
        #     for col in row:
        #         print(col, end=" ")
        #     print()
        n = len(grid)
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        target = n * n - 1
        def bfs(start, ub):
            # print(f"Processing bfs({start}, {ub})")
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
                    # print(f"{nr=}, {nc=}")
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= ub:
                        dq.append(nr * n + nc)
                        # print(f"Adding ({nr}, {nc}) to dq")
            return False

            # if grid[0][0] > ub:
            #     return False
            # dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            # path_exists = [False] * (n * n)
            # pq = [0]
            # while pq:
            #     u = pq.pop()
            #     if u == n * n - 1:
            #         return True
            #     path_exists[u] = True
            #     r, c = u // n, u % n
            #     for dr, dc in dirs:
            #         nr, nc = r + dr, c + dc
            #         if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] > ub:
            #             continue
            #         v = nr * n + nc
            #         if path_exists[v]:
            #             continue
            #         heapq.heappush(pq, v)
            # return path_exists[-1]

        

        res = max([max(row) for row in grid])
        l, r = 0, res
        while l <= r:
            m = (l + r) // 2
            exists = bfs(0, m)
            # print(f"bfs(0, {m}): {exists}")
            if exists:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
