class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        sum_all = sum(nums)
        sum_1_n = (n * (n+1)) // 2
        for num in nums:
            nums[abs(num)] *= -1
        sum_missing = 0
        num_missing = 0
        for i in range(1, n + 1):
            if nums[i] > 0:
                sum_missing += i
                num_missing += 1
        return (sum_all - sum_1_n + sum_missing) // (num_missing + 1)