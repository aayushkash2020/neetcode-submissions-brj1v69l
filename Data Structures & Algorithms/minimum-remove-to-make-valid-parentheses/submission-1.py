class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid = set()
        st = []
        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)
            elif ch == ')':
                if not st:
                    invalid.add(i)
                else:
                    st.pop()
        while st:
            invalid.add(st.pop())

        res = []
        for i, ch in enumerate(s):
            if i in invalid:
                continue
            res.append(ch)

        return "".join(res)
        # from collections import deque
        # ct = 0
        # res = deque()
        # for ch in s:
        #     if ch == '(':
        #         ct += 1
        #     elif ch == ')':
        #         if ct == 0:
        #             continue
        #         ct -= 1
        #     res.append(ch)
        # ct = 0
        # temp = "".join(res)
        # res2 = deque()
        # for i in range(len(temp)-1, -1, -1):
        #     ch = temp[i]
        #     if ch == ')':
        #         ct += 1
        #     elif ch == '(':
        #         if ct == 0:
        #             continue
        #         ct -= 1
        #     res2.appendleft(ch)
        # return "".join(res2)
            