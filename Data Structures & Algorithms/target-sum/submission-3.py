class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = defaultdict(int)
        def helper(end, target):
            if end == 0:
                if target == nums[0] and target == -nums[0]:
                    return 2
                if target == nums[0] or target == -nums[0]:
                    return 1
                return 0
    
            return helper(end - 1, target - nums[end]) + helper(end-1, target + nums[end])

            # if (start+1, target - nums[start]) not in cache:
            #     cache[(start+1, target - nums[start])] = helper(start+1, target - nums[start])
            # if (start+1, target + nums[start]) not in cache:
            #     cache[(start+1, target + nums[start])] = helper(start+1, target + nums[start])
            # return cache[(start+1, target - nums[start])] + cache[(start+1, target + nums[start])]
         
        return helper(n-1, target)

            