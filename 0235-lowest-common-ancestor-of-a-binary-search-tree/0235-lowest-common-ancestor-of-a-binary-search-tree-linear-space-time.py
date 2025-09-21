# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_parent = []
        q_parent = []
        def search(root, val):
            if not root:
                return
            
            if val == p.val:
                p_parent.append(root)
            elif val == q.val:
                q_parent.append(root)

            if root.val < val:
                search(root.right, val)
            elif root.val > val:
                search(root.left, val)
            else:
                return
        
        search(root, p.val)
        search(root, q.val)
        i,j=0,0
        res = None
        while i < len(p_parent) and j < len(q_parent):
            if p_parent[i].val == q_parent[j].val:
                res = p_parent[i]
            else:
                break
            i += 1
            j += 1
        
        if not res:
            return root
        
        return res
                
            
            