class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        begin = 0
        window = 0
        result = float('inf')

        for end in range(len(nums)):
            window += nums[end]

            while window >= target:
                result = min(result, end - begin + 1)
                window -= nums[begin]
                begin += 1
                
        return result if result != float('inf') else 0
