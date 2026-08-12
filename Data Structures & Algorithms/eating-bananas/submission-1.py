import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) - 1
        if h == len(piles):
            return r + 1
        res = r + 1
        while l <= r:
            k = l + (r - l) // 2
            time = sum(max(1, math.ceil(pile / k)) for pile in piles)
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res