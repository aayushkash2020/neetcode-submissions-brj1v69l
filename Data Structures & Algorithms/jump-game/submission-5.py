class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        l = h = 0
        while l <= h:
            l, h = h + 1, max(i + nums[i] for i in range(l, h+1))
            if h >= n-1:
                return True
        return False