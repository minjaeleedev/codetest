class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(1,n):
            # check one char
            if s[i] != '0':
                dp[i+1] += dp[i]
            
            # check two char
            if 10 <= int(s[i-1] + s[i]) <= 26:
                dp[i+1] += dp[i-1]
            
        return dp[n]