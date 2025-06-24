class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(num):
            if num == 1:
                return False
            
            s = 2
            while s*s <= num:
                if num % s == 0:
                    return False
                
                s += 1
            
            return True

        freq = Counter(nums)
        for k, v in freq.items():
            if is_prime(v):
                return True
        
        return False