class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        vol = 0
        while l < r:
            while heights[l] <= heights[r] and l < r:
                cur = (r - l) * heights[l]
                vol = max(vol, cur)
                l += 1
            while heights[r] <= heights[l] and l < r:
                cur = (r - l) * heights[r]
                vol = max(vol, cur)
                r -= 1
        return vol

            # while heights[l] <= heights[r] and l < r:
            #     if heights[l] == heights[r]:
            #         cur = (r - l) * heights[l]
            #         vol = max(vol, cur)
            #         r -= 1
            #     else:
            #         l += 1
            # cur = (r - l) * heights[r]
            # vol = max(vol, cur)
            # while heights[r] <= heights[l] and l < r:
            #     if heights[l] == heights[r]:
            #         cur = (r - l) * heights[l]
            #         vol = max(vol, cur)
            #         l += 1
            #     else:
            #         r -= 1
            # cur = (r - l) * heights[l]
            # vol = max(vol, cur)
        return vol
        # max_vol = 0
        # for i in range(len(heights) - 1):
        #     for j in range(i, len(heights), 1):
        #         vol = (j-i) * min(heights[i], heights[j])
        #         max_vol = max(max_vol, vol)
        # return max_vol