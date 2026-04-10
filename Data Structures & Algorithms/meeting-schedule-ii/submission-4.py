"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ints_heap = []
        intervals = sorted(intervals, key=lambda interval: interval.start)
        days = 0
        for interval in intervals:
            if len(ints_heap) > 0 and ints_heap[0] <= interval.start:
                heapq.heapreplace(ints_heap, interval.end)
            else:
                heapq.heappush(ints_heap, interval.end)
        return len(ints_heap)