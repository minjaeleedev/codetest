# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        last = head
        while last:
            last = last.next
            length += 1
        
        q, r = length//k, length%k
        result = []
        start = head
        while len(result) < k:
            if r > 0:
                arr_size = q+ 1
                r -= 1
            else:
                arr_size = q

            end = start
            for i in range(arr_size-1):
                end = end.next
            
            if end:
                tmp = end.next
                end.next = None
                result.append(start)
                start=tmp
            else:
                result.append(start)
            
        
        return result