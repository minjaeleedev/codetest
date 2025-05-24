# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(root, cur, s):
            if not root:
                return
            
            if not root.left and not root.right:
                if s + root.val == targetSum:
                    result.append(cur[:]+[root.val])
                    return

            cur.append(root.val)
            dfs(root.left, cur, s+root.val)
            dfs(root.right, cur, s+root.val)
            cur.pop()
            
        
        dfs(root, [], 0)
        return result