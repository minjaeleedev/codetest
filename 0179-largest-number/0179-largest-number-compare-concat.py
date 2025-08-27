from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a:str, b:str):
            short = min(len(a), len(b))
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            
            return 0
        
    
        nums = sorted(map(str, nums), key=cmp_to_key(cmp))

        return ''.join(nums) if nums[0] != '0' else '0'