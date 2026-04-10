from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = defaultdict(list)
        n = len(wordList)
        m = len(beginWord)

        for word in wordList:
            for i in range(m):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)

        dq = deque()
        dq.append((beginWord, 1))
        vis = set([beginWord])
        while dq:
            u, dist = dq.popleft()
            if u == endWord:
                return dist
            for i in range(m):
                pattern = u[:i] + "*" + u[i+1:]
                for v in patterns[pattern]:
                    if v not in vis:
                        vis.add(v)
                        dq.append((v, dist + 1))
                # patterns[pattern] = []
        
        return 0
            
            
