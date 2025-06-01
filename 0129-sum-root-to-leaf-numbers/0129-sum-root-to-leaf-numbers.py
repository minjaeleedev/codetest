# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur, result):
            if not root:
                return result
            
            if not root.left and not root.right:
                return cur * 10 + root.val
            
            left_result, right_result = 0, 0
            if root.left:
                left_result = dfs(root.left, cur*10 + root.val, result)
            if root.right:
                right_result = dfs(root.right, cur*10 + root.val, result)
            return left_result+right_result

        result = dfs(root, 0, 0)

        return result