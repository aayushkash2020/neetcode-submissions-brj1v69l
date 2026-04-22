# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        res = []
        while dq:
            cur_lvl = []
            cur_len = len(dq)
            for _ in range(cur_len):
                cur = dq.popleft()
                cur_lvl.append(cur.val)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            res.append(cur_lvl)
        return res
            