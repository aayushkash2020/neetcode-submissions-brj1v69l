class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # op & cl are # of open and close parentheses, respectively
        def rec(path, ls, op):
            if len(path) == 2*n:
                ls.append(''.join(path))
                return
            if op < n:
                path.append('(')
                rec(path, ls, op + 1)
                path.pop()
            if len(path) - op < op:
                path.append(')')
                rec(path, ls, op)
                path.pop()
        res = []
        rec([], res, 0)
        return res