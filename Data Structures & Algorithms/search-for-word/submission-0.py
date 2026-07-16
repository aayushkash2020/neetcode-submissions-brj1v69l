class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, path, visited = set()):
            if ''.join(path) == word:
                return True
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[len(path)] or (i, j) in visited:
                return False
            visited.add((i, j))
            path.append(board[i][j])
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if dfs(ni, nj, path, visited):
                    return True
            path.pop()
            visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, []):
                    return True
        return False