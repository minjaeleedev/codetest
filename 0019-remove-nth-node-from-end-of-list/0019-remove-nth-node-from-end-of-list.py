# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = head
        cnt = 0
        high = head
        low = None
        while high:
            if cnt == n:
                low = head
            elif cnt > n:
                low = low.next
                
            high = high.next
            cnt += 1
        
        if not low:
            # remove head
            result = result.next
        else:
            low.next = low.next.next
        
        return result