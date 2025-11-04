from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        for i in range(len(nums) - k + 1):
            cnt = list([(num, freq) for num, freq in Counter(nums[i : i + k]).items()])

            cnt.sort(key=lambda x: (-x[1], -x[0]))
            ls = list(map(lambda x: x[0] * x[1], cnt))

            answer.append(sum(ls[:x]))

        return answer
