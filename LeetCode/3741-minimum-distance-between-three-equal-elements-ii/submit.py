from collections import defaultdict
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ht = defaultdict(list)
        for i, n in enumerate(nums):
            ht[n].append(i)

        res = -1
        for k, arr in ht.items():
            for i in range(len(arr) - 2):
                dist = (arr[i + 2] - arr[i]) * 2
                res = min(dist, res) if res != -1 else dist

        return res
