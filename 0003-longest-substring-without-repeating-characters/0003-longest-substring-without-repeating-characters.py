class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        sub = ''
        for i in range(len(s)):
            c = s[i]
            if c in sub:
                idx = sub.find(c)
                sub = sub[idx+1:]
            
            sub += c
            result = max(result, len(sub))
            
        return result
            
            
        