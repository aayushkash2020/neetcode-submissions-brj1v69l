class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, n-1):
            prev, curr = curr, max(curr, prev + nums[i])
        res1 = curr
        prev, curr = nums[1], max(nums[1], nums[2])
        for i in range(3, n):
            prev, curr = curr, max(curr, prev + nums[i])
        return max(res1, curr)
        # n = len(nums)
        # if n <= 3:
        #     return max(nums)
        # dp = [[0] * 2 for _ in range(n+2)]
        # for j in range(1, -1, -1):
        #     for i in range(n-1, -1, -1):
        #         if i > j+n-2:
        #             dp[i][j] = 0
        #             continue
        #         keep = nums[i] + dp[i+2][j]
        #         skip = dp[i+1][j]
        #         dp[i][j] = max(keep, skip)
        # return max(dp[0][0], dp[1][1])