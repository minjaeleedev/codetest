from collections import deque
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        sq, lq = deque([]), deque([])
        eq_cnt = 0
        res = []
        for n in nums:
            if n == pivot:
                eq_cnt += 1
            elif n < pivot:
                sq.append(n)
            else:
                lq.append(n)
        
        while sq:
            res.append(sq.popleft())

        while eq_cnt:
            res.append(pivot)
            eq_cnt -= 1

        while lq:
            res.append(lq.popleft())
        
        return res