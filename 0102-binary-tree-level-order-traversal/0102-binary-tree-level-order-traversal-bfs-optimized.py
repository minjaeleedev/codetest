# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque([root]) if root else deque([])
        while q:
            same_lv = []
            for _ in range(len(q)):
                node = q.popleft()
                same_lv.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(same_lv)
            
        return result

