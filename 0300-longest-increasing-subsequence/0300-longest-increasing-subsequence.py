class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*(n+1)
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]: 
                    dp[i+1] = max(dp[i+1], dp[j+1]+1)
        
        return max(dp)
            