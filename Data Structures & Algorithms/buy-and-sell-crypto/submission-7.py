class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        b, s = 0, 1
        while s < len(prices):
            if prices[b] < prices[s]:
                res = max(res, prices[s] - prices[b])
            else:
                b = s
            s += 1
        return res

        # res = 0
        # b = 0
        # while b < len(prices) - 1:
        #     while b < len(prices) - 1 and prices[b] >= prices[b+1]:
        #         b += 1
        #     s = b
        #     while s < len(prices) - 1 and prices[s] <= prices[s+1]:
        #         s += 1
        #     res += prices[s] - prices[b]
        #     b = s+1
        # return res