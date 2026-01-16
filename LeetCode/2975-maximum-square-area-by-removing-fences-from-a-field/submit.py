from typing import List


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        hFences.extend([1, m])
        vFences.extend([1, n])
        hFences.sort()
        vFences.sort()

        lengths = set()
        for i in range(len(hFences) - 1):
            for j in range(i + 1, len(hFences)):
                lengths.add(hFences[j] - hFences[i])

        res = -1
        for i in range(len(vFences) - 1):
            for j in range(i + 1, len(vFences)):
                diff = vFences[j] - vFences[i]
                if diff in lengths:
                    res = max(diff, res)

        return res if res < 0 else (res**2) % (10**9 + 7)
