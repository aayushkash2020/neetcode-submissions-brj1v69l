class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        match = {'(': ')',
                 '{': '}',
                 '[': ']'
                }
        close = ')}]'

        for i, ch in enumerate(s):
            if ch in match:
                st.append(ch)
            if ch in close:
                if not st or ch != match[st[-1]]:
                    return False
                st.pop()
        return not st