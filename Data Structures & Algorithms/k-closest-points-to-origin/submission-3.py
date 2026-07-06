import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, (x, y) in enumerate(points):
            dst = math.sqrt(x * x + y * y)
            if len(heap) < k:
                heapq.heappush(heap, (-dst, i))
            else:                
                if dst < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-dst, i))
        return [points[idx] for _, idx in heap]