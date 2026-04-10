class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # m = Counter(s)
        # for c in t:
        #     if c not in m:
        #         return False
        #     m[c] -= 1
        #     if m[c] == 0:
        #         m.pop(c)
        # return len(m) == 0