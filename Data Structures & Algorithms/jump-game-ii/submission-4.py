class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def rec(idx):
            if idx >= len(nums) - 1:
                return 0
            if idx in memo:
                return memo[idx]
            best = len(nums)
            for i in range(nums[idx], 0, -1):
                best = min(best, 1 + rec(idx + i))
            memo[idx] = best
            return best
        return rec(0)