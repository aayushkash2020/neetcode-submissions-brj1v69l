class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = '+*-/'
        for t in tokens:
            if t not in ops:
                st.append(int(t))
                continue
            b = st.pop()
            a = st.pop()
            if t == '+':    
                st.append(a + b)
            elif t == '*':
                st.append(a * b)
            elif t == '-':
                st.append(a - b)
            else:
                st.append(int(a / b))
            print(f"result of op: {st[-1]}")
        
        return st[0]