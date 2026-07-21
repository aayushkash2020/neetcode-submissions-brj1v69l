class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        def rec(i, j):
            if i == m and j == n:
                return 0
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return rec(i+1, j+1)
            replace = rec(i+1, j+1)
            del1 = rec(i+1, j)
            del2 = rec(i, j+1)
            return 1 + min(replace, min(del1, del2))
        dp = [[0] * (n+1) for _ in range(m+1)]
        print(f"length: {len(dp)}, width: {len(dp[0])}")
        for i in range(m):
            dp[i][n] = m - i
        for j in range(n):
            dp[m][j] = n - j
        for i in range(m+1):
            for j in range(n+1):
                print(dp[i][j], end=" ")
            print()
        print('\n')
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                rep = dp[i+1][j+1]
                if word1[i] == word2[j]:
                    dp[i][j] = rep
                    continue
                del1 = dp[i+1][j]
                del2 = dp[i][j+1]
                dp[i][j] = 1 + min(rep, min(del1, del2))
        for i in range(m+1):
            for j in range(n+1):
                print(dp[i][j], end=" ")
            print()
        return dp[0][0]