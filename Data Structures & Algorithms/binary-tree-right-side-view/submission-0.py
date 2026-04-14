# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        done = set()
        res = []
        def dfs(root: Optional[TreeNode], depth: int) -> None:
            if not root:
                return
            if depth not in done:
                res.append(root.val)
                done.add(depth)
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)
        dfs(root, 0)
        return res
            