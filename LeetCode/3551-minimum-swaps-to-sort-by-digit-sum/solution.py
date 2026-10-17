from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n: int):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res

        n = len(nums)
        index = list(range(n))
        index.sort(key=lambda i: (digit_sum(nums[i]), nums[i]))

        target_pos = [0] * n
        for p, i in enumerate(index):
            target_pos[i] = p

        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = target_pos[j]

        return n - cycles
