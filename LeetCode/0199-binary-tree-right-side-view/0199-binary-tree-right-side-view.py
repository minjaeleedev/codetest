# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        by_lv = defaultdict(list)
        def traverse(root, lv):
            if not root:
                return
            
            traverse(root.left, lv+1)
            traverse(root.right, lv+1)
            by_lv[lv].append(root.val)
        
        traverse(root, 0)
        sorted_by_lv = sorted(by_lv.items(), key=lambda x:x[0])
        result = []
        for k, v in sorted_by_lv:
            result.append(v[-1])
        
        return result