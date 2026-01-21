from typing import List


# 3314에서 nums[i] 범위가 10^9이기 때문에 Brute Force로 풀면 TLE
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            ans = -1
            d = 1
            while d & n != 0:
                ans = n & ~d
                d <<= 1

            res.append(ans)

        return res
