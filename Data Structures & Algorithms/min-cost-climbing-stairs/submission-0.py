class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a, b = cost[-2], cost[-1]
        for i in range(n-3, -1, -1):
            a, b = cost[i] + min(a, b), a
        return min(a, b)