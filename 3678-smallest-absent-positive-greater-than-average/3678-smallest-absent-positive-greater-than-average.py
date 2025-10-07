class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        a = sum(nums)/len(nums)
        s = set(nums)
        res = 0
        for n in range(1, 102):
            if n > a and n not in s:
                res = n
                break
        
        return res
            