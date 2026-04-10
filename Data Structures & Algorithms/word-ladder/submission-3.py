from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = defaultdict(list)
        n = len(wordList)
        m = len(wordList[0])
        for i in range(m):
            pattern = beginWord[:i] + "*" + beginWord[i+1:]
            patterns[pattern].append(beginWord)

        for i, a in enumerate(wordList):
            for j in range(m):
                pattern = a[:j] + "*" + a[j+1:]
                patterns[pattern].append(a)

        for pattern in patterns:
            print(pattern, end="\t")
            print(patterns[pattern])

        dq = deque()
        dq.append(beginWord)
        dist = defaultdict(int)
        for w in wordList:
            dist[w] = float('inf')
        dist[beginWord] = 1
        while dq:
            u = dq.popleft()
            if u == endWord:
                return dist[u]
            for i in range(m):
                pattern = u[:i] + "*" + u[i+1:]
                for v in patterns[pattern]:
                    if dist[u] + 1 < dist[v]:
                        print("Relaxing ", v)
                        dist[v] = dist[u] + 1
                        print(f"dist[{v}] = {dist[v]}")
                        dq.append(v)
        
        return 0 if dist[endWord] == float('inf') else dist[endWord]
            
            
