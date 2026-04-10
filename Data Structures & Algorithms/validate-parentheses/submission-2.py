class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        match = {'(': ')',
                 '{': '}',
                 '[': ']'
                }
        close = ')}]'

        for ch in s:
            if ch in match:
                st.append(ch)
            else:
                if not st or ch != match[st[-1]]:
                    return False
                st.pop()
        return not st