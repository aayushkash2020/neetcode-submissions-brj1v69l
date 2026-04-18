class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(first):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                dfs(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        dfs(0)
        return res
        # n = len(nums)
        # res = []
        # seen = [False] * n
        # def dfs(path):
        #     if len(path) == n:
        #         res.append(path[:])
        #     for i in range(n):
        #         if not seen[i]:
        #             path.append(nums[i])
        #             seen[i] = True
        #             dfs(path)
        #             path.pop()
        #             seen[i] = False
        
        # dfs([])
        # return res