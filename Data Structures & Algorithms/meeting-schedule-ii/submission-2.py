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
        intervals = sorted(intervals, key=lambda interval: interval.end)
        days = 0
        for interval in intervals:
            if len(ints_heap) == 0 or interval.start < ints_heap[0]:
                days += 1
                heapq.heappush(ints_heap, interval.end)
            else:
                st = []
                while len(ints_heap) > 0 and interval.start > ints_heap[0]:
                    st.append(heapq.heappop(ints_heap))
                if len(st) > 0:
                    st.pop()
                while len(st) > 0:
                    heapq.heappush(ints_heap, st.pop())
                heapq.heappush(ints_heap, interval.end)
        return days
                

        return 0