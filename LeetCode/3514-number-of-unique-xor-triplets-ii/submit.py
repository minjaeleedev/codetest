from collections import defaultdict
from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        xors = defaultdict(int)
        for i in nums:
            for j in nums:
                xors[i ^ j] = 1

        res = defaultdict(int)
        for k in xors.keys():
            for n in nums:
                res[k ^ n] = 1

        return sum(res.values())
