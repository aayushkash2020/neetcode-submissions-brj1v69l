import heapq
class KthLargest:
    def _offer(self, val: int):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for val in nums:
            self._offer(val)

    def add(self, val: int) -> int:
        self._offer(val)
        return self.heap[0]
