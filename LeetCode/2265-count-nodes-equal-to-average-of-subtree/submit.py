# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def helper(node: TreeNode):
            if node is None:
                return (0, 0, 0)

            left_s, left_cnt, left_res = helper(node.left)
            right_s, right_cnt, right_res = helper(node.right)
            avg = (left_s + right_s + node.val) // (left_cnt + right_cnt + 1)
            cur_res = left_res + right_res + (1 if avg == node.val else 0)
            return (left_s + right_s + node.val, left_cnt + right_cnt + 1, cur_res)

        return helper(root)[2]
