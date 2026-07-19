class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        left = [0] * n
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            left[i] = st[-1] if st else -1
            st.append(i)
        st.clear()
        right = [0] * n
        for i in range(n-1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            right[i] = st[-1] if st else n
            st.append(i)
        res = 0
        for i in range(n):
            area = heights[i] * (right[i] - left[i] - 1)
            res = max(res, area)
        return res