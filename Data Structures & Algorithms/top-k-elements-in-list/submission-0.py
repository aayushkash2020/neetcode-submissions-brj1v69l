class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        b = {}
        for num in m:
            if m[num] not in b:
                b[m[num]] = []
            b[m[num]].append(num)
        res = []
        cur = len(nums)
        while k > 0:
            if cur not in b:
                cur -= 1
                continue
            res = res + b[cur]
            k -= len(b[cur])
            cur -= 1
        return res
