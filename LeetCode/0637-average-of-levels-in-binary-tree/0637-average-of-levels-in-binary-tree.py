# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lv = defaultdict(list)
        def helper(root, level:int):
            if not root:
                return
            
            lv[level].append(root.val)
            helper(root.left, level+1)
            helper(root.right, level+1)

        helper(root,0)
        result = []
        for k, v in sorted(lv.items(), key=lambda x:x[0]):
            result.append(v)
            
        return [sum(arr)/len(arr) for arr in result]