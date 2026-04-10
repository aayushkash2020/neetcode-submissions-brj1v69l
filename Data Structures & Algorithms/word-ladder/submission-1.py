from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        g = defaultdict(set)
        n = len(wordList)
        m = len(wordList[0])
        for i, a in enumerate(wordList):
            diffB = 0
            for idx in range(m):
                if a[idx] != beginWord[idx]:
                    diffB += 1
                if diffB > 1:
                    break
            if diffB == 1:
                g[a].add(beginWord)
                g[beginWord].add(a)

        for i, a in enumerate(wordList):
            for j in range(i+1, n):
                b = wordList[j]
                diff = 0
                for idx in range(m):
                    if a[idx] != b[idx]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    g[a].add(b)
                    g[b].add(a)
        
        for word in g:
            print(word, end="\t")
            print(g[word])

        dq = deque()
        dq.append(beginWord)
        dist = defaultdict(int)
        for w in wordList:
            dist[w] = float('inf')
        dist[beginWord] = 1
        while dq:
            print(dq)
            u = dq.popleft()
            for v in g[u]:
                if dist[u] + 1 < dist[v]:
                    print("Relaxing ", v)
                    dist[v] = dist[u] + 1
                    print(f"dist[{v}] = {dist[v]}")
                    dq.append(v)
        
        return 0 if dist[endWord] == float('inf') else dist[endWord]
            
            
