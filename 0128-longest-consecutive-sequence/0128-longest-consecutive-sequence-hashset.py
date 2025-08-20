class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        res = 0
        for n in uniq:
            if n-1 not in uniq:
                i = n + 1
                while i in uniq:
                    i += 1
                res = max(res, i-n)
        return res