class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        result = []
        cur = 0
        for num in nums:
            cur ^= num
        
        for i in range(len(nums)-1, -1, -1):
            k = 0
            for b in range(maximumBit):
                if cur & (1 << b):
                    continue
                
                k = k | (1 << b)

            result.append(k)
            cur ^= nums[i] 
            
        return result