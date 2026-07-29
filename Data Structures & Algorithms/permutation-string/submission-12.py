from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs = Counter(s1)
        m, n = len(s1), len(s2)
        l = 0
        remaining = len(freqs)
        for r in range(n):
            if s2[r] in freqs:
                freqs[s2[r]] -= 1
                if freqs[s2[r]] == 0:
                    remaining -= 1
            else:
                while l <= r:
                    if s2[l] in freqs:
                        if freqs[s2[l]] == 0:
                            remaining += 1
                        freqs[s2[l]] += 1
                    l += 1
            if r - l + 1 > m:
                if s2[l] in freqs:
                    if freqs[s2[l]] == 0:
                        remaining += 1
                    freqs[s2[l]] += 1
            if remaining == 0:
                return True
        return False