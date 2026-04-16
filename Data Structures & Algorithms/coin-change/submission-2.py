class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        cache = {}
        def helper(i, amount):
            if amount == 0:
                return 0
            if i == n:
                return -1
            if (i, amount) in cache:
                return cache[(i, amount)]
            keep = -1
            if coins[i] <= amount:
                keep = helper(i, amount - coins[i])
            skip = helper(i + 1, amount)
            if keep == -1 and skip == -1:
                res = -1
            elif keep == -1:
                res = skip
            elif skip == -1:
                res = 1 + keep
            else:
                res = min(skip, 1 + keep)
            cache[(i, amount)] = res
            return res

        return helper(0, amount)