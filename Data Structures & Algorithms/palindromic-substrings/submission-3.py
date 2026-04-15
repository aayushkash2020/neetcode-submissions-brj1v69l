class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

        # n = len(s)
        # dp = [False] * n
        # res = 0
        # for i in range(n-1, -1, -1):
        #     dp[i] = True
        #     res += 1
        #     for j in range(n-1, i, -1):
        #         dp[j] = (s[i] == s[j])
        #         if j > i + 1:
        #             dp[j] &= dp[j-1]
        #         res += 1 if dp[j] else 0
        # return res