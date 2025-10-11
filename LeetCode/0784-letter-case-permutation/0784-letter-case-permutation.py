class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def helper(s:str, cur: str, i:int):
            if len(cur) == len(s):
                result.append(cur)
                return
            
            nxt = s[i+1]
            if ord('a') <= ord(nxt) <= ord('z') or ord('A') <= ord(nxt) <= ord('Z'):
                low = nxt.lower()
                helper(s, cur+low, i+1)
                helper(s, cur+low.upper(), i+1)
            else:
                helper(s, cur+nxt, i+1)
            
            return 
        
        helper(s, "", -1)
        return result