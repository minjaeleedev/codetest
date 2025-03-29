class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        mn = min(nums)
        mn_filter = [n for n in nums if n != mn]
        arr = sorted(mn_filter)
        result = 0
        cnt = 0
        prev = -1 # not exist in number range
        for i, num in enumerate(arr):
            if prev != num:
                cnt += 1
            prev = num
            result += cnt

        return result
        
