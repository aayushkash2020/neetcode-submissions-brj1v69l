class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # op & cl are # of open and close parentheses, respectively
        def rec(path, ls, op, cl):
            if op + cl == 2*n:
                ls.append(''.join(path))
                return
            if op < n:
                path.append('(')
                rec(path, ls, op + 1, cl)
                path.pop()
            if cl < op:
                path.append(')')
                rec(path, ls, op, cl + 1)
                path.pop()
        res = []
        rec([], res, 0, 0)
        return res