class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur = 0
        for num in nums:
            cur ^= num
        return cur