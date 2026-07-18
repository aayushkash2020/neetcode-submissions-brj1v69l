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
            left = rec(root.left, lb, root.val)
            if root.left:
                left = left and lb < root.left.val < ub
            right = rec(root.right, root.val, ub)
            if root.right:
                right = right and lb < root.right.val < ub
            return left and right
        return rec(root, -float('inf'), float('inf'))