class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        res = []
        for n in nums:
            if n > 0:
                if n not in s:
                    res.append(n)
                    s.add(n)
        
        if not res:
            # all elements are negative
            return max(nums)
        
        return sum(res)