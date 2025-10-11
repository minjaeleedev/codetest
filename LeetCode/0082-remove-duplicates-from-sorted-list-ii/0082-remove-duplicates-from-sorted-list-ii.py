# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        cur = head
        is_dup = False
        prev = None
        while cur:
            e = cur.next
            is_dup = False
            while e and e.val == cur.val:
                is_dup = True
                e = e.next
            
            if is_dup:
                if not prev:
                    res = e
                else:
                    prev.next = e
            else:
                prev = cur
            
            cur = e

        return res