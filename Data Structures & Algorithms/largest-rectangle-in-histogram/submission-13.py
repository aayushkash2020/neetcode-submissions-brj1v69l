class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
        # while st:
        #     top = st.pop()
        #     lb = st[-1] if st else -1
        #     if lb >= 0 and heights[top] == heights[lb]:
        #         continue
        #     width = n - lb - 1
        #     res = max(res, heights[top] * width)
        return res