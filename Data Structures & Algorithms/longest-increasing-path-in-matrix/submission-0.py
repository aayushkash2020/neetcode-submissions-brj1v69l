class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dp = [[0] * m for _ in range(n)]
        def dfs(r, c):
            res = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < n or not 0 <= nc < m:
                    continue
                if matrix[nr][nc] <= matrix[r][c]:
                    continue
                tmp = matrix[r][c]
                matrix[r][c] = -1
                if dp[nr][nc] == 0:
                    res = max(res, 1 + dfs(nr, nc))
                else:
                    res = max(res, 1 + dp[nr][nc])
    
                matrix[r][c] = tmp
            
            dp[r][c] = res
            return res
        
        best = 1
        for r in range(n):
            for c in range(m):
                # if matrix[r][c] == -1:
                #     continue
                cur = None
                if dp[r][c] == 0:
                    cur = dfs(r,c)
                else:
                    cur = dp[r][c]

                best = max(best, cur)
        
        return best
        
