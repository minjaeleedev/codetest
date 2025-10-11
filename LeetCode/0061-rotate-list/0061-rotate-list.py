# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.length(head)
        if n == 0:
            return head
        
        rot = k % n
        progress = n - rot
        node = head
        prev_new_head = None
        while progress > 0 and node:
            prev_new_head = node if not prev_new_head else prev_new_head.next
            node = node.next
            progress -= 1
        
        if not node:
            return head
        
        new_head = node
        prev_new_head.next = None
        end = None
        it = new_head
        while it:
            end = it if not end else end.next
            it = it.next
        
        end.next = head
        return new_head
        
    def length(self, head: Optional[ListNode]) -> int:
        cur = head
        result = 0
        while cur:
            cur = cur.next
            result += 1
        
        return result
        