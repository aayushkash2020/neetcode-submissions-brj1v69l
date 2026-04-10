class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        a1 = [0] * 26
        for c in s1:
            a1[ord(c) - ord('a')] += 1
        a2 = [0] * 26
        l, r = 0, 0
        for r in range(len(s1)):
            a2[ord(s2[r]) - ord('a')] += 1
        while r < len(s2) - 1:
            if a1 == a2:
                return True
            a2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            a2[ord(s2[r]) - ord('a')] += 1
        return a1 == a2

        