class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur = nums[l] + nums[r]
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -= 1
        return res