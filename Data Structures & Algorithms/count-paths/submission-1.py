class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [0] * n
        for i in range(m):
            cur[-1] = 1
            for j in range(n-2, -1, -1):
                cur[j] += cur[j+1]
        return cur[0]