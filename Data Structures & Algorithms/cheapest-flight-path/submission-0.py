import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        weight = {}
        for u, v, price in flights:
            g[u].append((v, price))
        dist = [[float('inf')] * (k+2) for _ in range(n)]
        dist[src][0] = 0
        to_visit = [(0, src, 0)]
        while to_visit:
            d, u, stops = heapq.heappop(to_visit)
            if u == dst:
                return d
            if d > dist[u][stops] or stops > k:
                continue
            for v, price in g[u]:
                if dist[u][stops] + price < dist[v][stops+1]:
                    dist[v][stops+1] = dist[u][stops] + price
                    heapq.heappush(to_visit, (dist[v][stops+1], v, stops + 1))
        res = min(dist[dst])
        return res if res != float('inf') else -1




