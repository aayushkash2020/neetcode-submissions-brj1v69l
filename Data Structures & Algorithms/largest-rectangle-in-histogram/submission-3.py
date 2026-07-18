class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        for i in range(n):
            # print(f"Entering iteration {i}")
            best = 0
            ht = heights[i]
            j = k = i
            while j >= 0 and k < n:
                ht = min(ht, min(heights[j], heights[k]))
                area = ht * (k - j + 1)
                # print(f"Area for j={j}, k={k}: {area}")
                best = max(best, ht * (k - j + 1))
                j, k = j-1, k+1
            # print(f"best centered at index {i}: {best}")
            res = max(res, best)
            j, k = i, i+1
            if 0 <= j < k < n:
                ht = min(heights[j], heights[k])
            while j >= 0 and k < n:
                ht = min(ht, min(heights[j], heights[k]))
                area = ht * (k - j + 1)
                # print(f"Area for j={j}, k={k}: {area}")
                best = max(best, ht * (k - j + 1))
                j, k = j-1, k+1
            # print(f"best centered at index {(j+k)/2}: {best}")
            res = max(res, best)
        return res