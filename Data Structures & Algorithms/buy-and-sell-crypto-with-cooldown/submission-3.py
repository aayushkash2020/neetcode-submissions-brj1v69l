class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def rec(i: int, buying: bool) -> int:
            if i >= n:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            buy = None
            sell = None
            if buying:
                buy = -prices[i] + rec(i+1, False)
                cooldown = rec(i+1, True)
                best = max(buy, cooldown)
            else:
                sell = prices[i] + rec(i+2, True)
                cooldown = rec(i+1, False)
                best = max(sell, cooldown)
            dp[(i, buying)] = best
            return best
        return rec(0, True)
        # if memo is None:
        #     memo = {}
        # t_prices = tuple(prices)
        # if t_prices in memo:
        #     return memo[t_prices]
        # n = len(prices)
        # if n < 2:
        #     return 0
        # best = 0
        # lowest = prices[0]
        # for i in range(len(prices)):
        #     if prices[i] < lowest:
        #         lowest = prices[i]
        #     elif prices[i] > lowest:
        #         sell = prices[i] - lowest + self.maxProfit(prices[i+2:], memo)
        #         best = max(best, sell)
        # memo[t_prices] = best
        # return best