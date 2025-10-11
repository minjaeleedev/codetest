class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # while restoring prefix of two numbers, shift to right
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        
        return left << shift
