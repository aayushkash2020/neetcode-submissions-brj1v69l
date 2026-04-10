class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        b, s = 0, 0
        i = 0
        while i < len(prices):
            if prices[i] < prices[b]:
                res = max(res, prices[s] - prices[b])
                b, s = i, i
            elif prices[i] > prices[s]:
                s = i
            i += 1
        return max(res, prices[s] - prices[b])