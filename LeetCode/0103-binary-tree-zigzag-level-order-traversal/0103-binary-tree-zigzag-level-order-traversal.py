# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res =[]
        q = deque([])
        q.append(root)
        left = False
        while q:
            l = len(q)
            lv = []
            for i in range(l):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

                lv.append(cur.val)
                
            res.append(lv[::-1] if left else lv)
            left = not left
        
        return res