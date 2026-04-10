class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        locs = {}
        start = 0
        for i in range(len(s)):
            if s[i] in locs and locs[s[i]] >= start:
                res = max(res, i - start)
                start = locs[s[i]] + 1
            locs[s[i]] = i
        return max(res, len(s) - start)

