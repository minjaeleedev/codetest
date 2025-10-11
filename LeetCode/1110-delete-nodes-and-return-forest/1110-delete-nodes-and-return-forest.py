# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        result = []
        del_set = set(to_delete)
        if root.val not in del_set:
            result.append(root)
            
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
                if cur.left.val in del_set:
                    cur.left = None
            
            if cur.right:
                q.append(cur.right)
                if cur.right.val in del_set:
                    cur.right = None
            
            if cur.val in del_set:
                if cur.left:
                    result.append(cur.left)
                if cur.right:
                    result.append(cur.right)

        return result