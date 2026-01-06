from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q: deque[tuple[TreeNode, int]] = deque([])
        q.append((root, 1))
        res, s = 0, float("-inf")
        depth = 1
        while q:
            cur_s = 0
            while q and q[0][1] == depth:
                node, lv = q.popleft()
                if node.left:
                    q.append((node.left, lv + 1))
                if node.right:
                    q.append((node.right, lv + 1))
                cur_s += node.val

            if cur_s > s:
                res = lv
                s = max(s, cur_s)

            depth += 1

        return res
