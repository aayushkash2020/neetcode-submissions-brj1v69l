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
        areas = [0] * n
        res = 0
        for i in range(n):
            areas[i] = heights[i] * (right[i] - left[i] - 1)
            print(f"Found areas[{i}] = {areas[i]}")
            res = max(res, areas[i])
        return res
        # width = 0
        # cur = best = 0
        # for i in range(n):
        #     if st and heights[st[-1]] > heights[i]:
        #         best = max(best, cur + heights[st[0]] * (st[-1] - st[0] + 1))
        #     cur = 0
        #     while st and heights[st[-1]] > heights[i]:
        #         st.pop()
        #         cur += heights[i]
        #     st.append(i)
        # return best
            
        # n = len(heights)
        # res = 0
        # for i in range(n):
        #     # print(f"Entering iteration {i}")
        #     best = 0
        #     ht = heights[i]
        #     j = k = i
        #     while j >= 0 and k < n:
        #         ht = min(ht, min(heights[j], heights[k]))
        #         area = ht * (k - j + 1)
        #         # print(f"Area for j={j}, k={k}: {area}")
        #         best = max(best, ht * (k - j + 1))
        #         j, k = j-1, k+1
        #     # print(f"best centered at index {i}: {best}")
        #     res = max(res, best)
        #     j, k = i, i+1
        #     if 0 <= j < k < n:
        #         ht = min(heights[j], heights[k])
        #     while j >= 0 and k < n:
        #         ht = min(ht, min(heights[j], heights[k]))
        #         area = ht * (k - j + 1)
        #         # print(f"Area for j={j}, k={k}: {area}")
        #         best = max(best, ht * (k - j + 1))
        #         j, k = j-1, k+1
        #     # print(f"best centered at index {(j+k)/2}: {best}")
        #     res = max(res, best)
        # return res