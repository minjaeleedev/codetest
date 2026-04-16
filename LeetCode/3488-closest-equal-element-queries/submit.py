from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ht = defaultdict(list) # num to index.
        for i, n in enumerate(nums):
            ht[n].append(i)

        for k, v in ht.items():
            if len(v) == 1:
                continue

            v.sort()
        
        res = []
        for q in queries:
            arr = ht[nums[q]]
            if len(arr) == 1:
                res.append(-1)
                continue
            
            idx = bisect_left(arr, q)
            end_dist = len(nums) - arr[-1] + arr[0]
            dist1 = arr[idx+1] -arr[idx] if idx != len(arr) -1 else end_dist
            dist2 = arr[idx] -arr[idx-1] if idx != 0 else end_dist

            min_dist = min(dist1, dist2)
            res.append(min_dist)
        
        return res
            
