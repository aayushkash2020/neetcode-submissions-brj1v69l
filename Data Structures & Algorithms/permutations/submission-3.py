class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        seen = [False] * n
        def dfs(path):
            if len(path) == n:
                res.append(path[:])
            for i in range(n):
                if not seen[i]:
                    path.append(nums[i])
                    seen[i] = True
                    dfs(path)
                    path.pop()
                    seen[i] = False
        
        dfs([])
        return res