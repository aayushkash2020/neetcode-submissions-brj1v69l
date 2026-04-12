class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def helper(amount, i):
            if (amount, i) in cache:
                return cache[(amount, i)]
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            keep = 0
            if coins[i] <= amount:
                keep = helper(amount - coins[i], i)
            skip = helper(amount, i+1)
            res = keep + skip
            cache[(amount, i)] = res
            return res
        return helper(amount, 0)
        