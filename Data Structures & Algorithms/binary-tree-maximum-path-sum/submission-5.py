# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def print_tree(self, root: Optional[TreeNode]):
        if not root:
            return
        dq = deque([root])
        while dq:
            init_len = len(dq)
            for i in range(init_len):
                top = dq.popleft()
                if top:
                    print(top.val, end=" ")
                else:
                    print("None", end=" ")
                    continue
                if top.left:
                    dq.append(top.left)
                else:
                    dq.append(None)
                if top.right:
                    dq.append(top.right)
                else:
                    dq.append(None)
            print()

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.overall = float('-inf')
        def rec(node):
            if not node:
                return 0
            left = max(0, rec(node.left))
            right = max(0, rec(node.right))
            self.overall = max(self.overall, left + node.val + right)
            return node.val + max(left, right)
        rec(root)
        return self.overall