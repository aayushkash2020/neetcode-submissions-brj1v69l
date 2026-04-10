from collections import deque, defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = defaultdict(set)
        in_deg = [0] * 26
        letters_used = set()
        # Collect all letters used
        for w in words:
            for ch in w:
                letters_used.add(ch)        

        # Create adjacency list
        for i in range(n-1):
            a, b = words[i], words[i+1]
            # Check if dictionary is invalid - b is prefix of a
            if len(a) > len(b) and a.startswith(b):
                return ""
            to_check = min(len(a), len(b))
            for j in range(to_check):
                if a[j] != b[j]:
                    if b[j] not in adj[a[j]]:
                        in_deg[ord(b[j]) - ord('a')] += 1
                        adj[a[j]].add(b[j])
                    break
        
        # Kahn's algorithm
        res = []
        queue = deque()
        for ch in letters_used:
            if in_deg[ord(ch) - ord('a')] == 0:
                queue.append(ch)
        
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in adj[u]:
                idx = ord(v) - ord('a')
                in_deg[idx] -= 1
                if in_deg[idx] == 0:
                    queue.append(v)

        if len(res) != len(letters_used):
            return ""
        return ''.join(res)




