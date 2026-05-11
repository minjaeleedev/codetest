from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            st = []
            while n:
                st.append(n % 10)
                n //= 10

            while st:
                res.append(st.pop())

        return res
