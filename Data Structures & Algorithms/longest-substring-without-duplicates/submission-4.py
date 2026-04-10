class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        # res = 0
        # locs = {}
        # start = 0
        # for i in range(len(s)):
        #     if s[i] in locs and locs[s[i]] >= start:
        #         res = max(res, i - start)
        #         start = locs[s[i]] + 1
        #     locs[s[i]] = i
        # return max(res, len(s) - start)

