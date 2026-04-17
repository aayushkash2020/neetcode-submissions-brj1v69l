class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        found_n = False
        for num in nums:
            if abs(num) == n:
                found_n = True
            else:
                nums[abs(num)] *= -1
        if not found_n:
            return n
        print(nums)
        zero_idx = -1
        for i in range(n):
            if nums[i] > 0:
                return i
            if nums[i] == 0:
                zero_idx = i
        return zero_idx