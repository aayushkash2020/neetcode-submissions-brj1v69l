class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = defaultdict(int)
        def helper(end, target):
            if end == 0:
                return (target == nums[0]) + (target == -nums[0])

            if (end, target) not in cache:
                cache[(end, target)] = helper(end - 1, target - nums[end]) + helper(end - 1, target + nums[end])

            return cache[(end, target)]

        return helper(n-1, target)

            