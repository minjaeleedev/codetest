# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def helper(cur, pa, result):
            if not cur:
                return result
            
            if cur.left and pa and pa.val % 2 == 0:
                result += cur.left.val
            if cur.right and pa and pa.val % 2 == 0:
                result += cur.right.val
            
            result = helper(cur.left, cur, result) 
            result = helper(cur.right, cur, result)
            return result
        
        return helper(root, None, 0)