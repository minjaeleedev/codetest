class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        sub = ''
        for i in range(len(s)):
            c = s[i]
            if c not in sub:
                sub += c
            else:
                idx = sub.find(c)
                sub = sub[idx:i+1]
                
            result = max(result, len(sub))
            
        return result
            
            
        