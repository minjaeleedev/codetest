class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            temp = []
            for i in range(len(s)-1):
                temp.append(str((int(s[i])+int(s[i+1])) % 10))
            
            s = ''.join(temp)
        
        return s[0] == s[1]
