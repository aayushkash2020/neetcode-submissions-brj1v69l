class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(path, seen):
            if len(path) == n:
                res.append(path[:])
            for i in range(n):
                if i not in seen:
                    path.append(nums[i])
                    seen.add(i)
                    dfs(path, seen)
                    path.pop()
                    seen.remove(i)
            
        dfs([], set())
        return res