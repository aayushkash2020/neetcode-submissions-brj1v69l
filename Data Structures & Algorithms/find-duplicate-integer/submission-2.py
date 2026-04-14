class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            nums[abs(num)] *= -1


"""
n-x+1 #s appear once
1 # appears x times
x-2 #s appear 0 times
sum_all = 1+..+n - sum(x-2 #s that didn't appear) + (x-1) * repeated number
"""