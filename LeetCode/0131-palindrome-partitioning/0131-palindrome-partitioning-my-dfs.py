class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s:str):
            for i in range(len(s)//2):
                if s[i] != s[len(s)-i-1]:
                    return False
            
            return True
        
        result = []
        cur = []
        def dfs(s, j):
            if not s:
                result.append(cur[:])
                return
            elif len(s) == j:
                return

            sub = s[:j+1]
            if is_palindrome(sub):
                cur.append(sub)
                dfs(s[j+1:], 0)
                cur.pop()
            dfs(s, j+1)
            
        dfs(s, 0)
        return result