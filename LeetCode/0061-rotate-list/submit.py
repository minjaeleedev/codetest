from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        n = 0
        last = None
        while p:
            if p.next is None:
                last = p

            p = p.next
            n += 1

        if n == 0:
            return head

        rot = k % n
        if rot == 0:
            return head

        cnt = 0
        cur = head
        prev = None
        while cnt < n - rot:
            prev = cur
            cur = cur.next
            cnt += 1

        if prev:
            prev.next = None
        last.next = head
        head = cur
        return head
