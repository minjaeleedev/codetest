# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        BST의 inorder traverse는 strictly increasing이어야 함을 이용
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        values = inorder(root)
        # 오름차순인지 확인
        for i in range(1, len(values)):
            if values[i] <= values[i-1]:
                return False

        return True