import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = l + (r - l) // 2
            time = sum((pile + k - 1) // k for pile in piles)
            if time <= h:
                r = k
            else:
                l = k + 1
        return l