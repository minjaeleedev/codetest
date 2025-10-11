# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        lv = -1
        q = deque([(root,lv+1)])
        same = [root.val]
        while q:
            cur_node, cur_lv = q.popleft()
            if cur_lv != lv:
                res.append(same)
                same = []
                lv = cur_lv

            if cur_node.left:
                q.append((cur_node.left, lv+1))
                same.append(cur_node.left.val)
            if cur_node.right:
                q.append((cur_node.right, lv+1))
                same.append(cur_node.right.val)


        return res[::-1]