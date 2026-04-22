class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        new = intervals.sort(key = lambda x: x[1])
        res = 0
        cur_end = intervals[0][1]
        for i, (st, end) in enumerate(intervals[1:], 1):
            if st < cur_end:
                res += 1
            else:
                cur_end = end
        return res