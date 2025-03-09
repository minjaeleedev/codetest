# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            if len(heap) < k:
                heapq.heappush(heap, -root.val)
            traverse(root.right)
        
        traverse(root)
        return -heapq.heappop(heap)