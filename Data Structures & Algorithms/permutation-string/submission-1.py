class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        main = Counter(list(s1))
        for l in range(len(s2)-len(s1)+1):
            cur = Counter(list(s2[l:l+len(s1)]))
            if cur == main:
                return True
        return False