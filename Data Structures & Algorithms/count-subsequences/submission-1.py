class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = {}
        def rec(i, j, path):
            # i, j are positions within s & t, respectively
            if (i, j, path) in memo:
                return memo[(i, j, path)]
            if ''.join(path) == t:
                memo[(i, j, path)] = 1
                return 1
            if i >= m or j >= n:
                return 0
            skip = rec(i+1, j, path)
            if s[i] == t[j]:
                keep = rec(i+1, j+1, path + tuple(s[i]))
                memo[(i, j, path)] = keep + skip
            else:
                memo[(i, j, path)] = skip
            return memo[(i, j, path)]
        return rec(0, 0, ())