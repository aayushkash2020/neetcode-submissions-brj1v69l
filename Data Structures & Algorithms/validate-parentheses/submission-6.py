class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        close = {')': '(',
                 '}': '{',
                 ']': '['
                }

        for ch in s:
            if ch in close:
                if not st or close[ch] != st.pop():
                    return False
            else:
                st.append(ch)
                
        return not st