class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1]+n)

        res = 0
        l, h = 0, 1
        while h <= len(nums) and l < h:
            cur = prefix[h] - prefix[l]
            if cur >= target:
                if res == 0:
                    res = h - l
                else:
                    res = min(res, h-l)
                l += 1
            else:
                h += 1
        
        return res
                 
            