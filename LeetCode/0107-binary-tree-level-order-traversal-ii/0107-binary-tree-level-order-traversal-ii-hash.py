# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        to_lv = defaultdict(list)
        def traverse(root, lv):
            if not root:
                return
            
            traverse(root.left, lv+1)
            traverse(root.right, lv+1)
            to_lv[lv].append(root.val)

        traverse(root, 0)

        return [v for k, v in sorted(to_lv.items(), key=lambda x: -x[0])]