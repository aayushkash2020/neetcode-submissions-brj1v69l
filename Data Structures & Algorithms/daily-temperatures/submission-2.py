class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0] * n
        for i, temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                res[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        
        return res