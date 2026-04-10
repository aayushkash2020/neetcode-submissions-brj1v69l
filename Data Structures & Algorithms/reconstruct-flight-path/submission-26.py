class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            g[src].append(dst)


        res = []
        def dfs(src):
            while g[src]:
                dfs(g[src].pop())
            res.append(src)
        
        dfs("JFK")

        return res[::-1]

#         n = len(tickets)
#         g = defaultdict(list)
#         edge_counts = defaultdict(int)

#         # build graph with edge ids
#         for src, dst in tickets:
#             eid = edge_counts[(src, dst)]
#             g[src].append((dst, eid))
#             edge_counts[(src, dst)] += 1

#         # sort for lexicographic order
#         for src in g:
#             g[src].sort()

#         vis = set()
#         path = ["JFK"]

#         def dfs(u):
#             # if we've used all edges → done
#             if len(vis) == n:
#                 return True

#             for v, eid in g[u]:
#                 edge = (u, v, eid)
#                 if edge in vis:
#                     continue

#                 # take edge
#                 vis.add(edge)
#                 path.append(v)

#                 if dfs(v):
#                     return True

#                 # backtrack
#                 vis.remove(edge)
#                 path.pop()

#             return False

#         dfs("JFK")
#         return path
