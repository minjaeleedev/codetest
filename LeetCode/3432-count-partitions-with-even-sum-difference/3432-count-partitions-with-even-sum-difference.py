from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        result = 0
        for pref in prefix[:-1]:
            head = pref
            tail = prefix[-1] - head
            diff = head - tail
            if diff % 2 == 0:
                result += 1

        return result
