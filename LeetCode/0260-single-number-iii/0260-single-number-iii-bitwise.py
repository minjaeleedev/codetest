class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from functools import reduce
        x = reduce(lambda a, b: a ^ b, nums, 0)
        # rightmost bit
        y = x & -x
        return [
            reduce(lambda a, b: a ^ b, filter(lambda n: n & y, nums), 0),
            reduce(lambda a, b: a ^ b, filter(lambda n: not n & y, nums), 0)
        ]