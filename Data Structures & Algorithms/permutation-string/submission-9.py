class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        a1 = [0] * 26
        for c in s1:
            a1[ord(c) - ord('a')] += 1
        a2 = [0] * 26
        for r in range(len(s1)):
            a2[ord(s2[r]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            if a1[i] == a2[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            print(matches)
            if matches == 26:
                return True
            idx = ord(s2[r]) - ord('a')
            a2[idx] += 1
            if a2[idx] == a1[idx]:
                matches += 1
            elif a2[idx] - 1 == a1[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            a2[idx] -= 1
            if a2[idx] == a1[idx]:
                matches += 1
            elif a2[idx] + 1 == a1[idx]:
                matches -= 1
            l += 1
        return matches == 26
        # if len(s2) < len(s1):
        #     return False
        # a1 = [0] * 26
        # for c in s1:
        #     a1[ord(c) - ord('a')] += 1
        # a2 = [0] * 26
        # l, r = 0, 0
        # for r in range(len(s1)):
        #     a2[ord(s2[r]) - ord('a')] += 1
        # while r < len(s2) - 1:
        #     if a1 == a2:
        #         return True
        #     a2[ord(s2[l]) - ord('a')] -= 1
        #     l += 1
        #     r += 1
        #     a2[ord(s2[r]) - ord('a')] += 1
        # return a1 == a2