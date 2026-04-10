import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        total_len = m*n
        res = bisect.bisect_left(range(total_len), x=target, key=lambda idx: matrix[idx//n][idx%n])
        return 0 <= res < total_len and matrix[res//n][res%n] == target
        # m, n = len(matrix), len(matrix[0])
        # l, r = 0, m*n-1
        # while l <= r:
        #     mid = (l+r)//2
        #     i, j = (mid//n), mid % n
        #     if matrix[i][j] == target:
        #         return True
        #     elif matrix[i][j] < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return False




        # m, n = len(matrix), len(matrix[0])
        # i, j = 0, n - 1
        # while 0 <= i < m and 0 <= j < n:
        #     if matrix[i][j] == target:
        #         return True
        #     if target > matrix[i][j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return False