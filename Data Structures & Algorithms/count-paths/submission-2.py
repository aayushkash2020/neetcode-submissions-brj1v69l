class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = m + n - 2
        b = min(m-1, n-1)
        return math.comb(a, b)
        # cur = [0] * n
        # cur[-1] = 1
        # for i in range(m):
        #     for j in range(n-2, -1, -1):
        #         cur[j] += cur[j+1]
        # return cur[0]