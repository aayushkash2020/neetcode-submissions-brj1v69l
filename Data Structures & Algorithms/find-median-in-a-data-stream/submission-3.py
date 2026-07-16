import heapq
class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.stale = False
        self.med = None

    def addNum(self, num: int) -> None:
        med = self.findMedian()
        self.stale = True
        if med is None:
            heapq.heappush(self.minHeap, num)
            return
        if num < med or num == med and len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        diff = len(self.minHeap) - len(self.maxHeap)
        if -1 <= diff <= 1:
            return
        if diff > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        else:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if not self.stale:
            return self.med
        if self.minHeap and self.maxHeap:
            if len(self.minHeap) == len(self.maxHeap):
                # minus b/c maxHeap nums are negated
                self.med = (self.minHeap[0] - self.maxHeap[0]) / 2
            elif len(self.minHeap) > len(self.maxHeap):
                self.med = self.minHeap[0]
            else:
                self.med = -self.maxHeap[0]
        elif self.minHeap:
            self.med = self.minHeap[0]
        elif self.maxHeap:
            self.med = -self.maxHeap[0]
        self.stale = False
        return self.med