class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(x):
            if not x:
                return False
            for i in range(len(x)//2):
                if x[i] != x[len(x)-1-i]:
                    return False
            return True
        n = len(s)
        res = []
        def rec(i, cur_list, path):
            if i == n:
                if is_palindrome(path):
                    cur_list.append(''.join(path))
                    res.append(list(cur_list))
                    cur_list.pop()
                return
            if is_palindrome(path):
                # Add current path, reset from next index i + 1
                cur_list.append(''.join(path))
                rec(i+1, cur_list, [s[i]])
                cur_list.pop()
            # Continue current path
            path.append(s[i])
            rec(i+1, cur_list, path)
            path.pop()
        rec(0, [], [])
        return res
