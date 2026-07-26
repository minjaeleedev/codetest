from math import inf, prod
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min_arr = [inf] * 2
        max_arr = [-inf] * 3
        for n in nums:
            if n <= min_arr[0]:
                min_arr[1] = min_arr[0]
                min_arr[0] = n
            elif n <= min_arr[1]:
                min_arr[1] = n

            if n >= max_arr[0]:
                max_arr[2] = max_arr[1]
                max_arr[1] = max_arr[0]
                max_arr[0] = n
            elif n >= max_arr[1]:
                max_arr[2] = max_arr[1]
                max_arr[1] = n
            elif n >= max_arr[2]:
                max_arr[2] = n

        return max(min_arr[0] * min_arr[1] * max_arr[0], prod(max_arr))
