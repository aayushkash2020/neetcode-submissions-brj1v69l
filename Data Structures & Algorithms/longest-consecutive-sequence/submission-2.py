class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in range(len(nums)):
            num = nums[i]
            if num-1 not in s:
                j = num
                cur = 0
                while j in s:
                    cur += 1
                    j += 1
                longest = max(longest, cur)
        return longest
        
        
        # res = 0
        # start = dict()
        # end = dict()
        # for n in nums:
        #     start[n] = 1
        #     end[n] = 1
        #     if n+1 in start:
        #         start[n] += start[n+1]
        #         start.pop(n+1)
        #         new_len = end[n + start[n] - 1] + 1
        #         end[n + start[n] - 1] = new_len
        #         res = max(res, new_len)
        #     if n-1 in end:
        #         end[n] += end[n-1]
        #         end.pop(n-1)
        #         new_len = start[n - end[n] + 1] + 1
        #         start[n - end[n] + 1] = new_len
        #         res = max(res, new_len)

        # for st in start:
        #     print(st, ", ", start[st])
        # print()
        # for e in end:
        #     print(e, ", ", end[e])

        # return res

