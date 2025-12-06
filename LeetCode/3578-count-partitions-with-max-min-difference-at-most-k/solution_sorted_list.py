import bisect
from typing import List


class SortedList:
    def __init__(self) -> None:
        self._data = []

    def add(self, val) -> None:
        bisect.insort(self._data, val)

    def remove(self, val) -> None:
        idx = bisect.bisect_left(self._data, val)
        if idx < len(self._data) and self._data[idx] == val:
            self._data.pop(idx)
        else:
            raise ValueError(f"{val} not in SortedList")

    def __contains__(self, val) -> bool:
        index = bisect.bisect_left(self._data, val)
        return index < len(self._data) and self._data[index] == val

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, index: int):
        return self._data[index]

    def __repr__(self) -> str:
        return f"SortedList({self._data})"


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        cnt = SortedList()

        dp[0] = 1
        prefix[0] = 1

        j = 0
        for i in range(n):
            cnt.add(nums[i])
            # adjust window
            while j <= i and cnt[-1] - cnt[0] > k:
                cnt.remove(nums[j])
                j += 1
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod

        return dp[n]
