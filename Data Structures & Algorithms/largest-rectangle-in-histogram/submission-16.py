class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # This line ensures that the stack gets completely emptied at the end
        heights.append(0)
        n = len(heights)
        st = []
        left = [0] * n
        res = 0
        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                top = st.pop()
                lb = st[-1] if st else -1
                width = i - lb - 1
                res = max(res, heights[top] * width)
            st.append(i)
        return res