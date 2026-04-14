class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                dp[i][j] = (s[i] == s[j])
                if j > i + 1:
                    dp[i][j] &= dp[i+1][j-1]
        return sum(sum(dp[i]) for i in range(n))