class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n
        while cur != 1:
            tmp = 0
            while cur >= 1:
                tmp += (cur % 10) * (cur % 10)
                cur //= 10
            if tmp in seen:
                return False
            seen.add(tmp)
            cur = tmp
        return True