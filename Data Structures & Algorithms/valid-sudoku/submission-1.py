class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqs = collections.defaultdict(set)
        for r in range(n):
            for c in range(n):
                cur = board[r][c]
                if cur == ".":
                    continue
                if cur in rows[r] or cur in cols[c] \
                        or cur in sqs[(r // 3, c // 3)]:
                    return False
                rows[r].add(cur)
                cols[c].add(cur)
                sqs[(r // 3, c // 3)].add(cur)
        return True



