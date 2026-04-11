class Solution:
    def helper(self, nums: List[int], target: int, current: List[int],
                answers: set(List[int]), idx: int) -> None:
        if target == 0:
            answers.add(tuple(current))
            return
        if idx == len(nums):
            return
        self.helper(nums, target, current, answers, idx + 1)
        if nums[idx] <= target:
            current.append(nums[idx])
            self.helper(nums, target - nums[idx], current, answers, idx)
            current.pop()
        return

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answers = set()
        self.helper(nums, target, [], answers, 0)
        return [list(answer) for answer in answers]