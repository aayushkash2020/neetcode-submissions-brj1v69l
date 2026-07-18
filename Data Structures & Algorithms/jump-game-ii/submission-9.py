class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        frontier = 0
        farthest = 0
        jumps = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == frontier:
                jumps += 1
                frontier = farthest
        return jumps
        # memo = {}
        # def rec(idx):
        #     if idx >= len(nums) - 1:
        #         return 0
        #     if idx in memo:
        #         return memo[idx]
        #     best = len(nums)
        #     for i in range(nums[idx], 0, -1):
        #         best = min(best, 1 + rec(idx + i))
        #     memo[idx] = best
        #     return best
        # return rec(0)

        # n = len(nums)
        # dp = [0] * n
        # dp[-1] = 0
        # best = {}
        # best[n-1] = 0
        # for i in range(n-2, -1, -1):
        #     if nums[i] == 0:
        #         dp[i] = float('inf')
        #     else:
        #         dp[i] = 1 + min(dp[i+1:i+1+nums[i]])
        # return dp[0]
        