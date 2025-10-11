from collections import Counter
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = Counter(digits)
        result = 0
        for n in range(100, 999, 2):
            digit = Counter([n // 100, (n // 10) % 10, n % 10])
            even = True
            for k, v in digit.items():
                if cnt[k] < v:
                    even = False
                    break

            if even:
                result += 1

        return result
