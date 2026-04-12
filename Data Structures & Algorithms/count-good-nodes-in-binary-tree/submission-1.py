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
        ct = 1 if root.val >= biggest else 0
        biggest = max(biggest, root.val)
        return ct + self.helper(root.left, biggest) + self.helper(root.right, biggest)

    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, -float('inf'))