class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if n < m:
            s1, s2 = s2, s1
            m, n = n, m
        def rec(i, j):
            if i == m and j == n:
                return True
            if i < m and s1[i] == s3[i+j] and rec(i+1, j):
                return True
            if j < n and s2[j] == s3[i+j] and rec(i, j+1):
                return True
            return False
        dp = [[False] * (n+1) for _ in range(m+1)]
        for j in range(n, -1, -1):
            for i in range(m, -1, -1):
                a = i < m and s1[i] == s3[i+j] and dp[i+1][j]
                b = j < n and s2[j] == s3[i+j] and dp[i][j+1]
                dp[i][j] = a or b or i == m and j == n
        return dp[0][0]

        # return rec(0, 0)