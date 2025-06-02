# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(l):
            prev = None
            while l:
                temp = l
                rev = ListNode(temp.val)
                rev.next = prev
                prev = rev
                l = l.next
            
            return prev
        
        r1, r2 = reverse(l1), reverse(l2)
        result = None
        carry = 0
        while r1 and r2:
            v = r1.val + r2.val + carry
            carry = v//10
            node = ListNode(v%10)
            node.next = result
            result = node
            r1 = r1.next
            r2 = r2.next
        
        while r1:
            v = r1.val + carry
            carry = v//10
            node = ListNode(v%10)
            node.next = result
            result = node
            r1 = r1.next

        while r2:
            v = r2.val + carry
            carry = v//10
            node = ListNode(v%10)
            node.next = result
            result = node
            r2 = r2.next
        
        if carry:
            node = ListNode(carry)
            node.next = result
            result = node

        return result