from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s = set([int(n, 2) for n in nums])
        tmp = 0
        for i in range(2**n):
            if i not in s:
                tmp = i
                break

        result = bin(tmp)[2:]
        return "0" * (n - len(result)) + result
