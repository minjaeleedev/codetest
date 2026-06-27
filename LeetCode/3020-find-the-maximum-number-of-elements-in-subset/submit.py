from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for k, v in cnt.items():
            if k == 1:
                res = max(res, v if v % 2 else v - 1)
                continue

            cur = k
            mx = 0
            while cur in cnt:
                if cnt[cur] >= 2:
                    cur = cur**2
                    mx += 2
                else:
                    mx += 1
                    break

            res = max(mx if mx % 2 else mx - 1, res)

        return res
