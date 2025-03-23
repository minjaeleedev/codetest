# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        lv = defaultdict(list)
        def dfs(root, level):
            if not root:
                return
            
            lv[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        
        dfs(root, 0)
        return [v for k, v in sorted(lv.items(), key=lambda x:x[0])]
