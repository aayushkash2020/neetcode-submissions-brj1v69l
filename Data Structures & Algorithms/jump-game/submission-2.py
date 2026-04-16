class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        l = h = 0
        while l < n:
            h = l + nums[l]
            if h >= n-1:
                return True
            best = l + nums[l]
            best_j = l
            for j in range(l+1, h+1):
                if j + nums[j] > best:
                    best = j + nums[j]
                    best_j = j
            l = best_j
            if best == h:
                return False
        return True