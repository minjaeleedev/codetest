from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(key=lambda x: -x)
        s = sum(apple)
        res = 0
        for c in capacity:
            if s > 0:
                s -= c
                res += 1
            else:
                break

        return res
