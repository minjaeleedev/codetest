# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node: Optional[TreeNode], lv: int) -> tuple[bool, int]:
            if not node:
                return (True, lv)

            left = helper(node.left, lv + 1)
            right = helper(node.right, lv + 1)
            return (
                left[0] and right[0] and abs(left[1] - right[1]) <= 1,
                max(left[1], right[1]),
            )

        return helper(root, 0)[0]
