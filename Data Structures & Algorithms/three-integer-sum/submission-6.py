class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # -4, -1, -1, 0, 1, 2
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur = nums[l] + nums[r]
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -= 1
        return res
        # nums.sort()
        # res = []
        # l, r = 0, len(nums) - 1
        # while l < r - 1:
        #     target = -1 * (nums[l] + nums[r])
        #     if target > nums[r]:
        #         l += 1
        #         while l < r - 1 and nums[l] == nums[l-1]:
        #             l += 1
        #         continue
        #     if target < nums[l]:
        #         r -= 1
        #         while r > l + 1 and nums[r] == nums[r+1]:
        #             r -= 1
        #         continue
        #     if target < 0:
        #         i = l + 1
        #         while i < r:
        #             if nums[i] == target:
        #                 sol = [nums[l], nums[i], nums[r]]
        #                 res.append(sol)
        #                 break
        #             if nums[i] > target:
        #                 break
        #             i += 1
        #         r -= 1
        #         while r > l + 1 and nums[r] == nums[r+1]:
        #             r -= 1
        #     elif target >= 0:
        #         i = r - 1
        #         while i > l:
        #             if nums[i] == target:
        #                 sol = [nums[l], nums[i], nums[r]]
        #                 res.append(sol)
        #                 break
        #             if nums[i] < target:
        #                 break
        #             i -= 1
        #         l += 1
        #         while l < r - 1 and nums[l] == nums[l-1]:
        #             l += 1
        # return res

            