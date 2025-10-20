from collections import deque
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # mods = {0:[0, val], 1:[1, val+1] ...}
        mods = {i: deque([]) for i in range(value)}
        for n in nums:
            arr = mods[n % value]
            if len(arr) == 0:
                arr.append(n % value)
            else:
                arr.append(arr[-1] + value)

        is_conti = True
        res = -1
        while is_conti:
            for i in range(value):
                arr = mods[i]
                if len(arr) == 0:
                    is_conti = False
                    break
                else:
                    res = arr.popleft()

        return res + 1
