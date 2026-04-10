class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
                
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
                
        return res
        # res = 0
        # n = len(height)
        # maxLeft = [0] * n
        # maxRight = [0] * n
        # for i in range(1, n, 1):
        #     maxLeft[i] = max(maxLeft[i-1], height[i-1])
        #     maxRight[n-1-i] = max(maxRight[n-i], height[n-i])
            
        # for i, h in enumerate(height):
        #     res += max(min(maxLeft[i], maxRight[i]) - h, 0)
        # return res


        # res = 0
        # n = len(height)
        # l = 0
        # while l < n - 1:
        #     while l < n-1 and height[l+1] >= height[l]:
        #         l += 1
        #     r = l + 1
        #     end = r
        #     while r < n:
        #         if height[r] > height[r-1]:
        #             if r == n-1:
        #                 end = r
        #                 break
        #             elif height[r] > height[r+1]:
        #                 end = r
        #                 break
        #         elif r == n-1:
        #             return res
        #         r += 1
        #     top = min(height[l], height[end])
        #     for i in range(l+1, end, 1):
        #         res += top - height[i]
        #     l = end
        # return res
