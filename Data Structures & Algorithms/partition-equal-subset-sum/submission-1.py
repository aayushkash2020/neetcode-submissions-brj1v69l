class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        # def rec(i, target):
        #     if target == 0:
        #         return True
        #     if i == n:
        #         return False
        #     skip = rec(i+1, target)
        #     keep = False
        #     if nums[i] <= target:
        #         keep = rec(i+1, target - nums[i])
        #     return skip or keep
        # return rec(0, target)
        # 2D dp
        # dp = [[False] * (n+1) for _ in range(target+1)]
        # for i in range(n+1):
        #     dp[0][i] = True
        # for t in range(1, target+1):
        #     for i in range(n-1, -1, -1):
        #         skip = dp[t][i+1]
        #         keep = dp[t - nums[i]][i+1] if nums[i] <= t else False
        #         dp[t][i] = skip or keep
        # return dp[target][0]
        dp = [[False] * (target+1) for _ in range(n+1)]
        for t in range(target+1):
            dp[n][t] = False
        for i in range(n+1):
            dp[i][0] = True
        for i in range(n-1, -1, -1):
            for t in range(1, target+1):
                skip = dp[i+1][t]
                keep = dp[i+1][t-nums[i]] if nums[i] <= t else False
                dp[i][t] = skip or keep
        return dp[0][target]