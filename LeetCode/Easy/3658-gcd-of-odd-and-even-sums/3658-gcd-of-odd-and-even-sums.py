class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # maybe return n?
        def gcd(a:int,b:int)->int:
            if b == 0:
                return a
            
            return gcd(b, a%b)
        
        return gcd(n**2, n**2+n)
