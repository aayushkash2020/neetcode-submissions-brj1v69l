class Solution:
    def maxProfit(self, prices: List[int], memo=None) -> int:
        if memo is None:
            memo = {}
        t_prices = tuple(prices)
        if t_prices in memo:
            return memo[t_prices]
        n = len(prices)
        if n < 2:
            return 0
        best = 0
        lowest = prices[0]
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] > lowest:
                sell = prices[i] - lowest + self.maxProfit(prices[i+2:], memo)
                best = max(best, sell)
        memo[t_prices] = best
        return best