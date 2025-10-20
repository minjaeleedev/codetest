class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(0, len(s)-k):
            uniq = set(s[i:i+k])
            if len(uniq) != 1:
                continue
            
            before = i == 0 or s[i-1] != s[i]
            after = i+k == len(s)-1 or s[i] != s[i+k]
            if before and after:
                return True
        
        return False

                
