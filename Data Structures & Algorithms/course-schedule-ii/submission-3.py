from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = {}
        in_deg = [0] * numCourses
        for b, a in prerequisites:
            if a not in g:
                g[a] = []
            g[a].append(b)
            in_deg[b] += 1
        
        dq = deque()
        for i in range(numCourses):
            if in_deg[i] == 0:
                dq.append(i)
        res = []
        while dq:
            u = dq.popleft()
            res.append(u)
            if u not in g:
                continue
            for v in g[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    dq.append(v)

        if len(res) < numCourses:
            return []
        return res
        
