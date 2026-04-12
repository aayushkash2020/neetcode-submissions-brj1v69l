class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[amount]
        # cache = {}
        # def helper(amount, i):
        #     if amount == 0:
        #         return 1
        #     if i == len(coins):
        #         return 0
        #     if (amount, i) in cache:
        #         return cache[(amount, i)]
        #     keep = 0
        #     if coins[i] <= amount:
        #         keep = helper(amount - coins[i], i)
        #     skip = helper(amount, i+1)
        #     res = keep + skip
        #     cache[(amount, i)] = res
        #     return res
        # return helper(amount, 0)
        