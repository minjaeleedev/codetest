from math import inf
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def is_critical(p, c, n):
            if not p or not c or not n:
                return False

            return (p.val < c.val and c.val > n.val) or (
                p.val > c.val and c.val < n.val
            )

        p, c, n = None, head, head.next
        i = 0
        first = 0
        prev, cur = 0, 0
        min_d = inf
        while c:
            if is_critical(p, c, n):
                if not first:
                    first = i
                prev = cur
                cur = i
                if prev and cur:
                    min_d = min(min_d, cur - prev)

            p = c
            c = c.next
            n = c.next if c else None
            i += 1

        if not first or not prev:
            return [-1, -1]

        return [min_d, cur - first]
