from collections import deque
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque([])
        carry = 0
        n = len(digits)
        for i in range(n - 1, -1, -1):
            plus = digits[i] + carry + 1 if i == n - 1 else digits[i] + carry
            d = plus % 10
            carry = plus // 10
            res.appendleft(d)

        if carry == 1:
            res.appendleft(carry)

        return list(res)
