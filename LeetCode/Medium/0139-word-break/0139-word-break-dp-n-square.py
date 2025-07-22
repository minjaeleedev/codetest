class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # catsandog, [cat, cats, andog]
        # cats -> ''/cats, cat/s, ca/ts, c/ats, 
        # -> T, F, F, F
        n = len(s)
        store = set(wordDict)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            res = False
            for j in range(i):
                if not dp[j]:
                    continue
                latter = s[j:i]
                res = res or dp[j] and (latter in store)
            
            dp[i] = res
        
        return dp[n]
