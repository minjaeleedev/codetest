class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor_product = 0
        for num in nums:
            xor_product ^= num
        
        result = [0]*len(nums)
        mask = (1<<maximumBit) - 1
        for i in range(len(nums)):
            result[i] = xor_product ^ mask
            xor_product ^= nums[len(nums)-1-i] 
            
        return result