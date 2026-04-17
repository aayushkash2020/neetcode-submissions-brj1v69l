# Maintain pointers i and j fo s and p, respectively
# If we encounter a character in p followed by a '*', check result of:
#           * Moving i forward 1 and keeping j where it is (keep)
#               * can only do this if s[i] == s[j]
#           * Keeping i constant and moving j forward 2 (skip)
#               * equivalent to keeping 0 occurrences of that char 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        nxt = [False] * (n+1)
        nxt[-1] = True
        # Base cases
        for j in range(n-2, -1, -1):
            if j < n-1 and p[j+1] == '*':
                nxt[j] = nxt[j+2]
        # Regular case
        cur = [False] * (n+1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j < n - 1 and p[j+1] == '*':
                    skip = cur[j+2]
                    keep = ((s[i] == p[j]) or p[j] == '.') and nxt[j]
                    cur[j] = skip or keep
                elif s[i] == p[j] or p[j] == '.':
                    cur[j] = nxt[j+1]
            nxt, cur = cur, [False] * (n+1)

        return nxt[0]


        # m, n = len(s), len(p)
        # dp = [[False] * (n+1) for _ in range(m+1)]
        # dp[m][n] = True
        # # Base cases
        # for j in range(n-2, -1, -1):
        #     if j < n-1 and p[j+1] == '*':
        #         dp[m][j] = dp[m][j+2]
        # # Regular case
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if j < n - 1 and p[j+1] == '*':
        #             skip = dp[i][j+2]
        #             keep = ((s[i] == p[j]) or p[j] == '.') and dp[i+1][j]
        #             dp[i][j] = skip or keep
        #         elif s[i] == p[j] or p[j] == '.':
        #             dp[i][j] = dp[i+1][j+1]

        # return dp[0][0]

        # print(end="    ")
        # for j in range(len(dp[0])):
        #     print(j, end="      ")     
        # print()     
        # for i in range(len(dp)):
        #     print(i, end=":\t")
        #     for val in dp[i]:
        #         if val:
        #             print(val, end="   ")
        #         else:
        #             print(val, end="  ")
        #     print()
        


        # def rec(i, j):
        #     if i == m and j == n:
        #         return True
        #     if j == n:
        #         return False
        #     if i == m:
        #         if j < n-1 and p[j+1] == '*':
        #             return rec(i, j+2)
        #         return False
            
        #     if j < n - 1 and p[j+1] == '*':
        #         skip = rec(i, j+2)
        #         keep = rec(i+1, j)
        #         return skip or keep

        #     if s[i] == p[j] or p[j] == '.':
        #         return rec(i+1, j+1)
            
        #     return False

        # return rec(0, 0)
