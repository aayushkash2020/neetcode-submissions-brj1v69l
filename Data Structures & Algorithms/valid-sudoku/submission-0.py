class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        ## rows
        for i in range(n):
            cur = set()
            count = 0
            for j in range(n):
                if board[i][j] != '.':
                    cur.add(board[i][j])
                    count += 1
            if len(cur) != count:
                return False
        ## cols
        for i in range(n):
            cur = set()
            count = 0
            for j in range(n):
                if board[j][i] != '.':
                    cur.add(board[j][i])
                    count += 1
            if len(cur) != count:
                return False
        ## boxes
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                cur = set()
                count = 0
                for p in range(3):
                    for q in range(3):
                        if board[i+p][j+q] != ".":
                            cur.add(board[i+p][j+q])
                            count += 1
                if len(cur) != count:
                    return False
        
        return True






