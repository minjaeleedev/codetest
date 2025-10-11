class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            # Update twos: add bits that were in ones and now appear again
            twos = twos | (ones & num)
            
            # Update ones: toggle bits with XOR
            ones = ones ^ num
            
            # Clear bits that appear three times (present in both ones and twos)
            threes = ones & twos
            ones = ones & ~threes
            twos = twos & ~threes
        
        return ones
