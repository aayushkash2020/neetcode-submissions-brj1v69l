class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            f = [0] * 26
            for c in s:
                f[ord(c) - ord('a')] += 1
            f = tuple(f)
            if f in m:
                m[f].append(s)
            else:
                m[f] = [s]
        return list(m.values())
        # m = {}
        # for s in strs:
        #     s1 = ''.join(sorted(s))
        #     if s1 in m:
        #         m[s1].append(s)
        #     else:
        #         m[s1] = [s]
        # return list(m.values())