class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # op is # of open parentheses, respectively
        def rec(path, ls, op):
            if len(path) == 2*n:
                ls.append(''.join(path))
                return
            if op < n:
                path.append('(')
                rec(path, ls, op + 1)
                path.pop()
            if op > len(path) / 2:
                path.append(')')
                rec(path, ls, op)
                path.pop()
        res = []
        rec([], res, 0)
        return res