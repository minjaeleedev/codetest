from typing import List


class Seqs:
    def __init__(self):
        sample = "123456789"
        n = 10
        self.nums = nums = []

        for length in range(2, n):
            for start in range(n - length):
                nums.append(int(sample[start : start + length]))


class Solution:
    s = Seqs()

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [x for x in self.s.nums if x >= low and x <= high]
