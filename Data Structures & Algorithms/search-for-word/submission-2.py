class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j, idx, visited = set()):
            if idx == len(word):
                return True
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[idx] or (i, j) in visited:
                return False
            visited.add((i, j))
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if dfs(ni, nj, idx + 1, visited):
                    return True
            visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False