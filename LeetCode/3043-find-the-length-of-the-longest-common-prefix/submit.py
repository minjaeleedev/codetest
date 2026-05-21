from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def prefix(s1: str, s2: str) -> int:
            mn = min(len(s1), len(s2))
            res = 0
            for i in range(mn):
                if s1[i] == s2[i]:
                    res += 1
                else:
                    break

            return res

        arr2 = sorted([str(n) for n in arr2])
        res = 0
        for num in arr1:
            s = str(num)
            low, high = 0, len(arr2) - 1
            pref = 0
            while low <= high:
                mid = low + (high - low) // 2
                cur = prefix(s, arr2[mid])
                if cur > pref:
                    pref = cur
                if arr2[mid] > s:
                    high = mid - 1
                elif arr2[mid] == s:
                    break
                else:
                    low = mid + 1

            res = max(pref, res)

        return res
