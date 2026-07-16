import heapq
class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.stale = False
        self.med = None

    def addNum(self, num: int) -> None:
        print(f"Called addNum({num})")
        med = self.findMedian()
        self.stale = True
        if med is None:
            heapq.heappush(self.minHeap, num)
            print(f"After addNum({num}):\nbigger half: {self.minHeap}\nsmaller half: {self.maxHeap}")
            return
        if num < med or num == med and len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -num)
            print(f"Pushed {num} into maxHeap as {-num}")
        else:
            heapq.heappush(self.minHeap, num)
        diff = len(self.minHeap) - len(self.maxHeap)
        print(f"diff = {diff}")
        if -1 <= diff <= 1:
            print("heaps are balanced")
            return
        if diff > 1:
            print(f"popping from minHeap, pushing {-self.minHeap[0]} into maxHeap")
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        else:
            print(f"popping from maxHeap, pushing {-self.minHeap[0]} into minHeap")
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        print(f"After addNum({num}):\nbigger half: {self.minHeap}\nsmaller half: {self.maxHeap}")

    def findMedian(self) -> float:
        if not self.stale:
            print(f"self.stale is False, returning {self.med}")
            return self.med
        print(f"Executing findMedian, state of heaps:\nbigger half: {self.minHeap}\nsmaller half: {self.maxHeap}")
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
        print(f"returning {self.med}")
        return self.med