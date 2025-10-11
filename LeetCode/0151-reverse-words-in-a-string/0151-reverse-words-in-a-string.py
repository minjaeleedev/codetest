class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split()
        res = []
        for word in reversed(ls):
            if not word:
                continue
            
            res.append(word)
        
        return " ".join(res)