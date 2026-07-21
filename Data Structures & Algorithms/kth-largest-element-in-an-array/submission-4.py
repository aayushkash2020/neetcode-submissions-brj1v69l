import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            if l == r:
                return nums[l]
            pivot_idx = random.randint(l, r)
            nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            if p == n-k:
                return nums[p]
            if p < n-k:
                l = p + 1
            else:
                r = p - 1
            