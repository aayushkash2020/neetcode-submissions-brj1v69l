class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # op & cl are # of open and close parentheses, respectively
        def rec(path, ls, op, cl):
            if op + cl == 2*n:
                ls.append(path)
                return
            if op < n:
                path += '('
                rec(path, ls, op + 1, cl)
                path = path[:-1]
            if cl < op:
                path += ')'
                rec(path, ls, op, cl + 1)
                path = path[:-1]
        res = []
        rec("", res, 0, 0)
        return res