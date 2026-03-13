from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maxWorkerTimes = max(workerTimes)
        left, right, ans = (
            1,
            maxWorkerTimes * mountainHeight * (mountainHeight + 1) // 2,
            0,
        )
        eps = 1e-7

        while left <= right:
            mid = (left + right) // 2
            cnt = 0
            for t in workerTimes:
                work = mid // t
                # find the largest k such that 1+2+...+k <= work
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2 + eps)
                cnt += k
            if cnt >= mountainHeight:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
