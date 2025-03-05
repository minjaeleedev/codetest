class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # ()) -> add one ( -> 1
        # ( -> 1 () -> 0 ()) -> 1
        # )))((( -> 6
        result = 0
        cnt = 0
        for c in s:
            if c == '(':
                if cnt < 0:
                    result += abs(cnt)
                    cnt = 1
                else:
                    cnt += 1
            else:
                cnt -= 1
                
        if cnt != 0:
            result += abs(cnt)
        
        return result
        