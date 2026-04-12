# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: TreeNode, biggest: int) -> int:
        if not root:
            return 0
        if root.val >= biggest:
            biggest = root.val
            return 1 + self.helper(root.left, biggest) + self.helper(root.right, biggest)
        return self.helper(root.left, biggest) + self.helper(root.right, biggest)

    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, -101)