from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur = nums[0]
        res = 0
        last = None
        diff = -k
        for n in nums:
            if n != cur:
                cur = n
                # decide start diff
                d1 = last - n + 1
                d2 = -k
                diff = d2 if d1 < -k else d1

            if last is None or cur + diff != last:
                res += 1
                last = cur + diff

            if diff < k:
                diff += 1

        return res
