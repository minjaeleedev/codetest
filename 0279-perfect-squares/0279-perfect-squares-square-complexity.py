class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        i = 1
        while i*i <= n:
            dp[i*i] = 1
            i += 1
        
        for i in range(1, n+1):
            if dp[i] == 1:
                continue
            
            j = 1
            while j**2 <= i:
                if dp[i] == 0:
                    dp[i] = dp[i-j**2] + dp[j]
                else:
                    dp[i] = min(dp[i], dp[i-j**2] + dp[j**2])
                
                j += 1

        return dp[n]