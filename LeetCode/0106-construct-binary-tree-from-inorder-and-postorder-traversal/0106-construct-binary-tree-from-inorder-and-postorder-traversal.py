# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_idx = {n : i for i, n in enumerate(inorder)}
        def helper(il, ih, pl, ph):
            if il > ih:
                return None

            val = postorder[ph]
            idx = in_idx[val]
            l_cnt = idx - il
            new_node = TreeNode(val)
            new_node.left = helper(il, idx-1, pl, pl+l_cnt-1)
            new_node.right = helper(idx+1, ih, pl+l_cnt, ph-1)
            return new_node
            
            
        res = helper(0, len(inorder)-1, 0, len(postorder)-1)
        return res