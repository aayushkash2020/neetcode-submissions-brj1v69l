class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        # memo = {}
        # def rec(i, j):
        #     # i, j are positions within s & t, respectively
        #     if j == n:
        #         return 1
        #     if i == m:
        #         return 0
        #     skip = rec(i+1, j)
        #     if s[i] == t[j]:
        #         keep = rec(i+1, j+1)
        #         return keep + skip
        #     else:
        #         return skip
        # return rec(0, 0)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][n] = 1
        for j in range(n):
            dp[m][j] = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                skip = dp[i+1][j]
                if s[i] == t[j]:
                    keep = dp[i+1][j+1]
                    dp[i][j] = keep + skip
                else:
                    dp[i][j] = skip
        return dp[0][0] 