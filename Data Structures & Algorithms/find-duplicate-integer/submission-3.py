class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            nums[abs(num)] *= -1