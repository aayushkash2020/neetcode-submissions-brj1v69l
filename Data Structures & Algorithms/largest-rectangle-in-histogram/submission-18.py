class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # This line ensures that the stack gets completely emptied at the end since
        # when the loop reaches i = n, it will just keep popping from the stack until
        # it's empty, as all heights are > 0, and calculate the area for each height.
        heights.append(0)
        n = len(heights)
        st = []
        left = [0] * n
        res = 0
        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                top = st.pop()
                # For the element at heights[pop], the closest smaller element on the left
                # occurs at the next index in the stack (if it exists, otherwise -1), lb.
                # The closest smaller element on the right is at heights[i] since that is
                # the first element that caused it to be popped off of the stack. So, the
                # rectangle with height height[top] has width i - lb - 1 (since i and lb
                # are excluded from the rectangle).
                lb = st[-1] if st else -1
                width = i - lb - 1
                res = max(res, heights[top] * width)
            st.append(i)
        return res