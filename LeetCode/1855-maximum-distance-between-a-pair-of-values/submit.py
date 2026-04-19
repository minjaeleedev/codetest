from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        res = 0
        while i < len(nums1) and j < len(nums2):
            if i <= j and nums1[i] <= nums2[j]:
                # valid
                res = max(res, j - i)
                j += 1
                continue

            if i < j:
                i += 1
            else:
                i = j + 1
                j = i

        return res
