# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)

        slow = head
        prev_slow = ListNode()
        prev_slow.next = slow
        fast = head
        while fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next
            if fast and fast.next:
                fast=fast.next
        
        prev_slow.next = None
        new_node = TreeNode(slow.val)
        new_node.left = self.sortedListToBST(head)
        new_node.right = self.sortedListToBST(slow.next)
        return new_node