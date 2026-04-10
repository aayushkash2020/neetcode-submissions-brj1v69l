class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        m = len(beginWord)
        front = {beginWord}
        back = {endWord}
        steps = 1
        while front and back:
            if len(front) > len(back):
                front, back = back, front
            newFront = set()
            for word in front:
                for i in range(m):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in back:
                            return steps + 1
                        if newWord in wordSet:
                            newFront.add(newWord)
                            wordSet.remove(newWord)
            steps += 1
            front = newFront

        return 0

        # if endWord not in wordList:
        #     return 0
        # patterns = defaultdict(list)
        # n = len(wordList)
        # m = len(beginWord)

        # for word in wordList:
        #     for i in range(m):
        #         pattern = word[:i] + "*" + word[i+1:]
        #         patterns[pattern].append(word)

        # dq = deque()
        # dq.append((beginWord, 1))
        # vis = set([beginWord])
        # while dq:
        #     u, dist = dq.popleft()
        #     if u == endWord:
        #         return dist
        #     for i in range(m):
        #         pattern = u[:i] + "*" + u[i+1:]
        #         for v in patterns[pattern]:
        #             if v not in vis:
        #                 vis.add(v)
        #                 dq.append((v, dist + 1))
        #         # patterns[pattern] = []
        
        # return 0
            
            
