class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dp = [[0] * m for _ in range(n)]
        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]
            res = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < n or not 0 <= nc < m:
                    continue
                if matrix[nr][nc] <= matrix[r][c]:
                    continue
                
                res = max(res, 1 + dfs(nr, nc))
    
            dp[r][c] = res
            return res
        
        best = 1
        for r in range(n):
            for c in range(m):
                best = max(best, dfs(r, c))
        
        return best
        
