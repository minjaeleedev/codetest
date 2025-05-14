# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0, 0
            
            if not root.left and not root.right:
                val = root.val
                root.val = 0
                return val, 0
            
            ls, lr = helper(root.left)
            rs, rr = helper(root.right)
            val = root.val
            diff = abs(ls-rs)
            root.val = diff
            return val + ls + rs, diff + lr + rr
        
        val, res = helper(root)
        return res