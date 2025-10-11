class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s:str)->str:
            prev = s[0]
            res = ''
            cnt = 1
            for i in range(1,len(s)):
                if prev == s[i]:
                    cnt += 1
                else:
                    res = res + str(cnt) + prev
                    prev = s[i]
                    cnt = 1
            
            res += str(cnt) + prev
            return res
        
        if n == 1:
            return "1"
        
        return rle(self.countAndSay(n-1))