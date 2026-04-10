class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        res = "".join(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, st = 0, 0
        while i < len(s):
            if s[i] == '#':
                l = int(s[st:i])
                res.append(s[i+1:i+1+l])
                i = i+l+1
                st = i
            else:
                i += 1
        return res
