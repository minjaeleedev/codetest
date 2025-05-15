# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, result):
            if not root:
                return result
            
            result[root.val] += 1
            result = helper(root.left, result)
            result = helper(root.right, result)
            return result
        
        res = helper(root, defaultdict(int))
        mx = max(res.values())
        
        return [k for k, v in res.items() if v == mx]
        
        