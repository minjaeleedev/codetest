# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low_head = None
        low_tail = low_head
        high_head = None
        high_tail = high_head
        it = head
        while it:
            if it.val < x:
                if low_head is None:
                    low_head = ListNode(it.val)
                    low_tail = low_head
                else:
                    low_tail.next = ListNode(it.val)
                    low_tail = low_tail.next
            else:
                if high_head is None:
                    high_head = ListNode(it.val)
                    high_tail = high_head
                else:
                    high_tail.next = ListNode(it.val)
                    high_tail = high_tail.next
            
            it = it.next

        if low_tail:
            low_tail.next = high_head
            
        return low_head or high_head