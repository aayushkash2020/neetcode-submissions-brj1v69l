class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(l, r):
            if l > r:
                return False
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        n = len(s)
        # res = final result
        res = []
        # path represents the current partition
        path = []
        def dfs(i):
            if i == n:
                # Append a shallow copy of the current path
                res.append(path[:])
                return
            # For each of the indices i...n-1, if s[i:j+1] is a palindrome, then set end of current block to be j, then recurse
            for j in range(i, n):
                if is_palindrome(i, j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return res
