from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def prefix(root: Optional[TreeNode]):
            if not root:
                return 0

            cur = root.val
            if root.left:
                cur += prefix(root.left)
            if root.right:
                cur += prefix(root.right)

            root.val = cur
            return cur

        prefix(root)

        def dfs(root: Optional[TreeNode], mx: int, res: int):
            if not root:
                return res

            a = mx - root.val
            res = max(res, root.val * a)
            res = dfs(root.left, mx, res)
            res = dfs(root.right, mx, res)
            return res

        return dfs(root, root.val, 0) % (10**9 + 7)
