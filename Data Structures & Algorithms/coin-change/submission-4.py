class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        cur = [-1] * (amount + 1)
        cur[0] = 0
        for i in range(n-1, -1, -1):
            for amt in range(1, amount+1):
                keep = -1
                if coins[i] <= amt:
                    keep = cur[amt - coins[i]]
                skip = cur[amt]
                if keep == -1 and skip == -1:
                    res = -1
                elif keep == -1:
                    res = skip
                elif skip == -1:
                    res = 1 + keep
                else:
                    res = min(skip, 1 + keep)
                cur[amt] = res
        return cur[amount]
            # cache = {}
        # def helper(i, amount):
        #     if amount == 0:
        #         return 0
        #     if i == n:
        #         return -1
        #     if (i, amount) in cache:
        #         return cache[(i, amount)]
            # keep = -1
            # if coins[i] <= amount:
            #     keep = helper(i, amount - coins[i])
            # skip = helper(i + 1, amount)
            # if keep == -1 and skip == -1:
            #     res = -1
            # elif keep == -1:
            #     res = skip
            # elif skip == -1:
            #     res = 1 + keep
            # else:
            #     res = min(skip, 1 + keep)
            # cache[(i, amount)] = res
            # return res

        # return helper(0, amount)