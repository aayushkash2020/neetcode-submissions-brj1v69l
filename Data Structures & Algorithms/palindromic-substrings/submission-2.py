class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [False] * n
        res = 0
        for i in range(n-1, -1, -1):
            dp[i] = True
            res += 1
            for j in range(n-1, i, -1):
                dp[j] = (s[i] == s[j])
                if j > i + 1:
                    dp[j] &= dp[j-1]
                res += 1 if dp[j] else 0
        return res