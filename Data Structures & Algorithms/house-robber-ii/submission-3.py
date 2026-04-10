class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        dp = [[0] * 2 for _ in range(n+2)]
        for j in range(1, -1, -1):
            for i in range(n-1, -1, -1):
                if i > j+n-2:
                    dp[i][j] = 0
                    continue
                keep = nums[i] + dp[i+2][j]
                skip = dp[i+1][j]
                dp[i][j] = max(keep, skip)
        return max(dp[0][0], dp[1][1])
    