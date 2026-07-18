# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root, lb, ub):
            if not root:
                return True
            if not (lb < root.val < ub):
                return False
            leftValid = rec(root.left, lb, root.val)
            rightValid = rec(root.right, root.val, ub)
            return leftValid and rightValid
        return rec(root, -float('inf'), float('inf'))