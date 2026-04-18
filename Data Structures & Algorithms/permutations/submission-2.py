class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(path, seen):
            if len(path) == n:
                res.append(path[:])
            for i in range(n):
                if not seen[i]:
                    path.append(nums[i])
                    seen[i] = True
                    dfs(path, seen)
                    path.pop()
                    seen[i] = False
        seen = [False] * n
        dfs([], seen)
        return res