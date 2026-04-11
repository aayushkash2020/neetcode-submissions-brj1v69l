class Solution:
    def helper(self, nums: List[int], target: int, current: List[int],
                answers: List[List[int]], idx: int) -> None:
        if target == 0:
            answers.append(current[:])
            return
        if idx == len(nums):
            return
        if nums[idx] > target:
            return
        self.helper(nums, target, current, answers, idx+1)
        if nums[idx] <= target:
            current.append(nums[idx])
            self.helper(nums, target - nums[idx], current, answers, idx)
            current.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answers = []
        nums.sort()
        self.helper(nums, target, [], answers, 0)
        return answers