# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_helper(node, mn, mx):
            if not node:
                return True
            
            if not (node.val > mn and node.val < mx):
                return False
            
            return validate_helper(node.left, mn, node.val) and validate_helper(node.right, node.val, mx)
        
        return validate_helper(root, float('-inf'), float('inf'))