class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        
        dp = [False] * (n+1)
        dp[0] = True
        
        for j in range(1, n+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n+1):
                con1 = dp[j] and s1[i-1] == s3[i+j-1]
                con2 = dp[j-1] and s2[j-1] == s3[i+j-1]
                dp[j] = con1 or con2
                
        return dp[n]