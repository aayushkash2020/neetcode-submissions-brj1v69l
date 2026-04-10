class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            if c not in m:
                m[c] = 0
            m[c] += 1
        for c in t:
            if c not in m:
                return False
            m[c] -= 1
            if m[c] == 0:
                m.pop(c)
        return len(m) == 0