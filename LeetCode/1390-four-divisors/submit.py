from collections import defaultdict
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        mem = defaultdict(int)

        # O(n sqrt m)
        def four_divisor(n: int) -> int:
            if n in mem:
                return mem[n]

            i = 1
            divisors = []
            while i * i <= n:
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)

                i += 1

            if len(divisors) == 4:
                return sum(divisors)

            return 0

        res = 0
        for n in nums:
            s = four_divisor(n)
            res += s

        return res
