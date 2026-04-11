# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEqual(self, root: Optional[TreeNode], other: Optional[TreeNode]) -> bool:
        if not root and not other:
            return True
        elif not root or not other or root.val != other.val:
            return False
        return self.isEqual(root.left, other.left) and self.isEqual(root.right, other.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        return self.isEqual(root, subRoot) or \
            self.isSubtree(root.left, subRoot) or \
            self.isSubtree(root.right, subRoot)